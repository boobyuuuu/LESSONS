# 日记页面

<style>
  /* 1 整体风格 */
  body {
    background: url('https://cdn.pixabay.com/photo/2022/06/13/12/19/sea-7259914_1280.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: 'xiaokai', sans-serif;
    margin: 0;
    padding: 0;
  }
  h1, h2, h3, h4, h5, h6 {
    font-weight: normal !important;
  }
  h1::before, h1::after, h2::after, h3::after, h4::after, h5::after, h6::after {
    content: none !important;
  }
  p r {
    color: inherit !important;
  }
  h1 {
    font-weight:bold;
    text-align: center;
    font-size: 2.5em;
    padding: 10px;
    border-radius: 8px;
    font-family: 'xiaokai', sans-serif;
  }
  h2 {
    text-align: center;
    font-size: 2em;
    background-color: #ffc7c7;
    padding: 8px;
    border-radius: 8px;
    font-family: 'xiaokai', sans-serif;
  }
    .section-title {
    text-align: center;
    font-size: 1.6em;
    background-color: #ffc7c7;
    padding: 10px;
    border-radius: 8px;
    font-family: 'xiaokai', sans-serif;
    margin-top: 20px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
  }
  th {
    background-color: #ffe2e2;
  }
  tr:nth-child(even) {
    background-color: #ffe2e2;
  }
  tr:hover {
    background-color: #ddd;
  }
  /* 2 日历 */
  .calendar {
    font-family: 'xiaokai', sans-serif;
  }
  .current-date {
    text-align: center;
    font-size: 1.5em;
    margin-bottom: 10px;
    cursor: pointer;
  }
  .date-selector {
    display: none;
    text-align: center;
    margin-bottom: 10px;
  }
  .date-selector select {
    font-size: 1em;
  }
  .entries {
    margin-top: 20px;
  }
  .entry {
    margin-bottom: 20px;
    position: relative;
  }
  .entry h2 {
    font-size: 1.5em;
    margin-bottom: 10px;
    display: inline-block;
  }
  .entry .delete-button {
    position: absolute;
    right: 10px;
    top: 10px;
    background-color: #ffe2e2;
    color: black;
    border: none;
    border-radius: 5px;
    padding: 5px 10px;
    cursor: pointer;
  }
  .entry textarea {
    width: 100%;
    height: 200px;
    font-size: 1em;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
  }
  .export-import-buttons {
    text-align: center;
    margin-bottom: 20px;
  }
  .export-import-buttons button {
    margin: 0 10px;
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
  }
</style>

<script>
document.addEventListener("DOMContentLoaded", function() {
    const calendar = document.querySelector(".calendar");

    function saveEntries() {
      const entries = document.querySelectorAll(".entry");
      const entriesData = {};
      entries.forEach(entry => {
        const date = entry.dataset.date;
        const content = entry.querySelector("textarea").value;
        entriesData[date] = content;
      });
      localStorage.setItem("diaryEntries", JSON.stringify(entriesData));
    }

    function loadEntries() {
      const entriesData = JSON.parse(localStorage.getItem("diaryEntries")) || {};
      for (const date in entriesData) {
        const newEntry = document.createElement("div");
        newEntry.className = "entry";
        newEntry.dataset.date = date;
        newEntry.innerHTML = `<h2>${date}</h2><button class="delete-button">删除</button><textarea placeholder="写下你的日记...">${entriesData[date]}</textarea>`;
        document.querySelector(".entries").appendChild(newEntry);
      }
      sortEntries();
      addDeleteEventListeners();
    }

    function sortEntries() {
      const entriesContainer = document.querySelector(".entries");
      const entries = Array.from(entriesContainer.children);
      entries.sort((a, b) => new Date(a.dataset.date) - new Date(b.dataset.date));
      entries.forEach(entry => entriesContainer.appendChild(entry));
    }

    function addDeleteEventListeners() {
      const deleteButtons = document.querySelectorAll(".delete-button");
      deleteButtons.forEach(button => {
        button.addEventListener("click", (event) => {
          const entry = event.target.closest(".entry");
          const date = entry.dataset.date;
          if (confirm(`是否删除 ${date} 的日记？`)) {
            entry.remove();
            saveEntries();
          }
        });
      });
    }

    function generateCalendar(calendarElement, year, month) {
      const now = new Date();
      const currentYear = year || now.getFullYear();
      const currentMonth = month || now.getMonth();
      const date = now.getDate();
      const firstDay = new Date(currentYear, currentMonth, 1).getDay();
      const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

      let calendarHTML = `<div class="current-date">${currentYear}年${currentMonth + 1}月${date}日</div>`;
      calendarHTML += '<div class="date-selector"><select class="year-selector">';
      for (let y = currentYear - 10; y <= currentYear + 10; y++) {
        calendarHTML += `<option value="${y}" ${y === currentYear ? 'selected' : ''}>${y}</option>`;
      }
      calendarHTML += '</select><select class="month-selector">';
      for (let m = 0; m < 12; m++) {
        calendarHTML += `<option value="${m}" ${m === currentMonth ? 'selected' : ''}>${m + 1}月</option>`;
      }
      calendarHTML += '</select></div>';
      calendarHTML += '<table><thead><tr>';
      const daysOfWeek = ['日', '一', '二', '三', '四', '五', '六'];
      daysOfWeek.forEach(day => {
        calendarHTML += `<th>${day}</th>`;
      });
      calendarHTML += '</tr></thead><tbody><tr>';

      for (let i = 0; i < firstDay; i++) {
        calendarHTML += '<td></td>';
      }

      for (let day = 1; day <= daysInMonth; day++) {
        if ((firstDay + day - 1) % 7 === 0) {
          calendarHTML += '</tr><tr>';
        }
        calendarHTML += `<td class="calendar-day">${day}</td>`;
      }

      calendarHTML += '</tr></tbody></table>';
      calendarElement.innerHTML = calendarHTML;

      const days = calendarElement.querySelectorAll(".calendar-day");
      days.forEach(day => {
        day.addEventListener("click", () => {
          const selectedDate = `${currentYear}年${currentMonth + 1}月${day.textContent}日`;
          document.querySelector(".current-date").textContent = selectedDate;
          const entry = document.querySelector(`.entry[data-date="${currentYear}-${currentMonth + 1}-${day.textContent}"]`);
          if (entry) {
            entry.scrollIntoView({ behavior: "smooth" });
          } else {
            const newEntry = document.createElement("div");
            newEntry.className = "entry";
            newEntry.dataset.date = `${currentYear}-${currentMonth + 1}-${day.textContent}`;
            newEntry.innerHTML = `<h2>${selectedDate}</h2><button class="delete-button">删除</button><textarea placeholder="写下你的日记..."></textarea>`;
            document.querySelector(".entries").appendChild(newEntry);
            sortEntries();
            newEntry.scrollIntoView({ behavior: "smooth" });
            addDeleteEventListeners();
          }
        });
      });

      document.querySelector(".current-date").addEventListener("click", () => {
        document.querySelector(".date-selector").style.display = 'block';
      });

      document.querySelector(".year-selector").addEventListener("change", (event) => {
        const selectedYear = parseInt(event.target.value);
        const selectedMonth = parseInt(document.querySelector(".month-selector").value);
        generateCalendar(calendarElement, selectedYear, selectedMonth);
      });

      document.querySelector(".month-selector").addEventListener("change", (event) => {
        const selectedMonth = parseInt(event.target.value);
        const selectedYear = parseInt(document.querySelector(".year-selector").value);
        generateCalendar(calendarElement, selectedYear, selectedMonth);
      });
    }

    function exportEntries() {
      const entriesData = JSON.parse(localStorage.getItem("diaryEntries")) || {};
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(entriesData));
      const downloadAnchorNode = document.createElement('a');
      downloadAnchorNode.setAttribute("href", dataStr);
      downloadAnchorNode.setAttribute("download", "diaryEntries.json");
      document.body.appendChild(downloadAnchorNode);
      downloadAnchorNode.click();
      downloadAnchorNode.remove();
    }

    function importEntries(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
          const importedData = JSON.parse(e.target.result);
          const existingData = JSON.parse(localStorage.getItem("diaryEntries")) || {};
          const mergedData = { ...existingData, ...importedData };
          localStorage.setItem("diaryEntries", JSON.stringify(mergedData));
          document.querySelector(".entries").innerHTML = '';
          loadEntries();
        };
        reader.readAsText(file);
      }
    }

    window.addEventListener("beforeunload", saveEntries);
    loadEntries();
    generateCalendar(calendar);

    document.querySelector("#export-button").addEventListener("click", exportEntries);
    document.querySelector("#import-input").addEventListener("change", importEntries);
});
</script>

<div class="export-import-buttons">
  <button id="export-button">导出</button>
  <input type="file" id="import-input" style="display: none;">
  <button onclick="document.getElementById('import-input').click();">导入</button>
</div>
<div>
  <div class="calendar"></div>
  <div class="entries"></div>
</div>

