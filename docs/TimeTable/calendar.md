# 2025年1月任务表

<style>
  body {
    background: url('https://cdn.pixabay.com/photo/2022/06/13/12/19/sea-7259914_1280.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: 'xiaokai', sans-serif;
    margin: 0;
    padding: 0;
  }
  .container {
    background-color: #f6f6f6;
    border-radius: 10px;
    box-shadow: 0 4px 6px #ffe2e2;
    padding: 20px;
    margin: 20px auto;
    max-width: 800px;
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
    /* background-color: rgba(233, 174, 184, 0.8); */
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
  .comment-input, .progress-input, .rating-input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: 'xiaokai', sans-serif;
    transition: border-color 0.3s, box-shadow 0.3s;
  }
  .comment-input:focus, .progress-input:focus, .rating-input:focus {
    border-color: #ffe2e2;
    box-shadow: 0 0 5px #ffe2e2;
    outline: none;
  }
  .tooltip {
    display: none;
    position: absolute;
    background-color: #fff;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 4px;
    box-shadow: 0 0 10px #f6f6f6;
    z-index: 1000;
    max-width: 300px;
    font-family: 'xiaokai', sans-serif;
  }
  .progress-bar-container {
    width: 100%;
    background-color: #f6f6f6;
    border-radius: 10px;
    overflow: hidden;
    height: 10px;
    margin-top: 5px;
    cursor: pointer; /* Add cursor change */
  }
  .progress-bar {
    height: 100%;
    background-color: #ffc7c7;
    width: 0;
    transition: width 0.3s;
    border-radius: 10px;
  }
  .calendar {
    display: none;
    position: absolute;
    background-color: #fff;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 4px;
    box-shadow: 0 0 10px #f6f6f6;
    z-index: 1000;
    font-family: 'xiaokai', sans-serif;
  }
  .calendar table {
    width: 100%;
    border-collapse: collapse;
  }
  .calendar th, .calendar td {
    border: 1px solid #ddd;
    padding: 5px;
    text-align: center;
    cursor: pointer;
  }
  .calendar .completed {
    background-color: #ffc7c7;
  }
  .calendar .completed::after {
    content: "✔"; /* Add checkmark */
    color: green;
    font-size: 1.2em;
    margin-left: 5px;
  }
  .calendar-input {
    width: 100%;
    padding: 5px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: 'xiaokai', sans-serif;
    transition: border-color 0.3s, box-shadow 0.3s;
    display: none; /* Hide input by default */
  }
  .calendar-input:focus {
    border-color: #ffe2e2;
    box-shadow: 0 0 5px #ffe2e2;
    outline: none;
  }
  .calendar-day {
    position: relative;
  }
  .calendar-day:hover .calendar-input {
    display: block; /* Show input on hover */
  }
  .calendar-day:hover .calendar-date {
    display: none; /* Hide date on hover */
  }
  .calendar-date {
    display: block;
  }
  .calendar-comment {
    display: inline-block;
    width: 20px;
    height: 20px;
    background-color: #ffc7c7;
    border-radius: 4px;
    text-align: center;
    line-height: 20px;
    cursor: pointer;
    margin-left: 5px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
  }
  .calendar-comment:hover .tooltip {
    display: block; /* Show tooltip on hover */
  }
</style>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const commentInputs = document.querySelectorAll(".comment-input");
    const progressInputs = document.querySelectorAll(".progress-input");
    const ratingInputs = document.querySelectorAll(".rating-input");
    const progressBars = document.querySelectorAll(".progress-bar");
    const checkboxes = document.querySelectorAll("input[type='checkbox']");
    const tooltip = document.createElement("div");
    tooltip.className = "tooltip";
    document.body.appendChild(tooltip);
    const calendars = document.querySelectorAll(".calendar");
    const calendarInputs = document.querySelectorAll(".calendar-input");

    // 恢复勾选框的状态
    checkboxes.forEach((checkbox, index) => {
      const savedChecked = localStorage.getItem(checkbox-${index});
      if (savedChecked === "true") {
        checkbox.checked = true;
      } else {
        checkbox.checked = false;
      }

      checkbox.addEventListener("change", () => {
        localStorage.setItem(checkbox-${index}, checkbox.checked);
      });
    });

    // 处理注释、进度、评级的本地存储
    function handleMouseOver(event, input) {
      if (input.value.length > input.size) {
        tooltip.textContent = input.value;
        tooltip.style.display = "block";
        tooltip.style.left = event.pageX + "px";
        tooltip.style.top = event.pageY + "px";
      }
    }

    function handleMouseOut() {
      tooltip.style.display = "none";
    }

    commentInputs.forEach((input, index) => {
      const savedValue = localStorage.getItem(comment-${index});
      if (savedValue) {
        input.value = savedValue;
      }
      input.addEventListener("input", () => {
        localStorage.setItem(comment-${index}, input.value);
      });
      input.addEventListener("mouseover", (event) => handleMouseOver(event, input));
      input.addEventListener("mouseout", handleMouseOut);
    });

    progressInputs.forEach((input, index) => {
      const savedValue = localStorage.getItem(progress-${index});
      if (savedValue) {
        input.value = savedValue;
        progressBars[index].style.width = savedValue + "%";
      }
      input.addEventListener("input", () => {
        const value = input.value;
        localStorage.setItem(progress-${index}, value);
        progressBars[index].style.width = value + "%";
      });
    });

    ratingInputs.forEach((input, index) => {
      const savedValue = localStorage.getItem(rating-${index});
      if (savedValue) {
        input.value = savedValue;
      }
      input.addEventListener("input", () => {
        localStorage.setItem(rating-${index}, input.value);
      });
      input.addEventListener("mouseover", (event) => handleMouseOver(event, input));
      input.addEventListener("mouseout", handleMouseOut);
    });

    progressBars.forEach((progressBar, index) => {
      progressBar.addEventListener("click", (event) => {
        const calendar = calendars[index];
        calendar.style.display = "block";
        calendar.style.left = event.pageX + "px";
        calendar.style.top = event.pageY + "px";
      });
      progressBar.parentElement.style.cursor = "pointer"; // Add cursor change
    });

    document.addEventListener("click", (event) => {
      if (!event.target.classList.contains("progress-bar") && !event.target.closest(".calendar")) {
        calendars.forEach(calendar => {
          calendar.style.display = "none";
        });
      }
    });

    calendars.forEach((calendar, index) => {
      const days = calendar.querySelectorAll("td");
      days.forEach(day => {
        day.addEventListener("click", () => {
          day.classList.toggle("completed");
          const completedDays = Array.from(days).filter(d => d.classList.contains("completed")).map(d => d.textContent);
          localStorage.setItem(completedDays-${index}, JSON.stringify(completedDays));
        });
      });

      const savedCompletedDays = JSON.parse(localStorage.getItem(completedDays-${index}) || "[]");
      savedCompletedDays.forEach(day => {
        const dayElement = Array.from(days).find(d => d.textContent === day);
        if (dayElement) {
          dayElement.classList.add("completed");
        }
      });
    });

    calendarInputs.forEach((input, index) => {
      const savedValue = localStorage.getItem(calendar-input-${index});
      if (savedValue) {
        input.value = savedValue;
        const commentBox = input.nextElementSibling;
        commentBox.textContent = savedValue;
        commentBox.style.display = "inline-block";
      }
      input.addEventListener("input", () => {
        const value = input.value;
        localStorage.setItem(calendar-input-${index}, value);
        const commentBox = input.nextElementSibling;
        commentBox.textContent = value;
        commentBox.style.display = value ? "inline-block" : "none";
      });
      input.addEventListener("mouseover", (event) => handleMouseOver(event, input));
      input.addEventListener("mouseout", handleMouseOut);
    });

    document.querySelectorAll(".calendar-comment").forEach((commentBox, index) => {
      commentBox.addEventListener("mouseover", (event) => {
        const input = document.querySelector(.calendar-input[data-day="${commentBox.dataset.day}"]);
        handleMouseOver(event, input);
      });
      commentBox.addEventListener("mouseout", handleMouseOut);
    });

    function generateCalendar() {
      const date = new Date();
      const year = date.getFullYear();
      const month = date.getMonth();
      const daysInMonth = new Date(year, month + 1, 0).getDate();
      let calendarHTML = "<table><tr>";
      const daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
      daysOfWeek.forEach(day => {
        calendarHTML += <th>${day}</th>;
      });
      calendarHTML += "</tr><tr>";
      const firstDay = new Date(year, month, 1).getDay();
      for (let i = 0; i < firstDay; i++) {
        calendarHTML += "<td></td>";
      }
      for (let day = 1; day <= daysInMonth; day++) {
        if ((firstDay + day - 1) % 7 === 0) {
          calendarHTML += "</tr><tr>";
        }
        calendarHTML += <td class="calendar-day"><span class="calendar-date">${day}</span><input type="text" class="calendar-input" placeholder="添加注释" size="10" data-day="${day}"><span class="calendar-comment" data-day="${day}"></span></td>;
      }
      calendarHTML += "</tr></table>";
      return calendarHTML;
    }

    calendars.forEach(calendar => {
      calendar.innerHTML = generateCalendar();
    });

    calendars.forEach((calendar, index) => {
      const days = calendar.querySelectorAll("td");
      days.forEach(day => {
        day.addEventListener("click", () => {
          day.classList.toggle("completed");
          const completedDays = Array.from(days).filter(d => d.classList.contains("completed")).map(d => d.textContent);
          localStorage.setItem(completedDays-${index}, JSON.stringify(completedDays));
        });
      });

      const savedCompletedDays = JSON.parse(localStorage.getItem(completedDays-${index}) || "[]");
      savedCompletedDays.forEach(day => {
        const dayElement = Array.from(days).find(d => d.textContent === day);
        if (dayElement) {
          dayElement.classList.add("completed");
        }
      });
    });
  });
</script>

<div class="container">

  <div class="section-title">长期任务：重要但不紧急</div>

  <table>
    <thead>
      <tr>
        <th>事件</th>
        <th>状态</th>
        <th>注释</th>
        <th>进度</th>
        <th>评级</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>健身</td>
        <td><input type="checkbox"></td>
        <td><input type="text" class="comment-input" placeholder="添加注释" size="20"></td>
        <td><input type="number" class="progress-input" placeholder="0-100"><div class="progress-bar-container"><div class="progress-bar"></div></div><div class="calendar"></div></td>
        <td><input type="text" class="rating-input" placeholder="输入评级" size="20"></td>
      </tr>
      <tr>
        <td>考研</td>
        <td><input type="checkbox"></td>
        <td><input type="text" class="comment-input" placeholder="添加注释" size="20"></td>
        <td><input type="number" class="progress-input" placeholder="0-100"><div class="progress-bar-container"><div class="progress-bar"></div></div><div class="calendar"></div></td>
        <td><input type="text" class="rating-input" placeholder="输入评级" size="20"></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">近期任务：紧急且很重要</div>

  <table>
    <thead>
      <tr>
        <th>事件</th>
        <th>状态</th>
        <th>注释</th>
        <th>进度</th>
        <th>评级</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>超分辨项目</td>
        <td><input type="checkbox"></td>
        <td><input type="text" class="comment-input" placeholder="添加注释" size="20"></td>
        <td><input type="number" class="progress-input" placeholder="0-100"><div class="progress-bar-container"><div class="progress-bar"></div></div><div class="calendar"></div></td>
        <td><input type="text" class="rating-input" placeholder="输入评级" size="20"></td>
      </tr>
      <tr>
        <td>LHAASO项目</td>
        <td><input type="checkbox"></td>
        <td><input type="text" class="comment-input" placeholder="添加注释" size="20"></td>
        <td><input type="number" class="progress-input" placeholder="0-100"><div class="progress-bar-container"><div class="progress-bar"></div></div><div class="calendar"></div></td>
        <td><input type="text" class="rating-input" placeholder="输入评级" size="20"></td>
      </tr>
      <tr>
        <td>天昊项目</td>
        <td><input type="checkbox"></td>
        <td><input type="text" class="comment-input" placeholder="添加注释" size="20"></td>
        <td><input type="number" class="progress-input" placeholder="0-100"><div class="progress-bar-container"><div class="progress-bar"></div></div><div class="calendar"></div></td>
        <td><input type="text" class="rating-input" placeholder="输入评级" size="20"></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="section-title">短期事务：紧急但不重要</div>

  <table>
    <thead>
      <tr>
        <th>事件</th>
        <th>状态</th>
        <th>注释</th>
        <th>进度</th>
        <th>评级</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>朗阁退钱</td>
        <td><input type="checkbox"></td>
        <td><input type="text" class="comment-input" placeholder="添加注释" size="20"></td>
        <td><input type="number" class="progress-input" placeholder="0-100"><div class="progress-bar-container"><div class="progress-bar"></div></div><div class="calendar"></div></td>
        <td><input type="text" class="rating-input" placeholder="输入评级" size="20"></td>
      </tr>
      <tr>
        <td>学生证与校园卡</td>
        <td><input type="checkbox"></td>
        <td><input type="text" class="comment-input" placeholder="添加注释" size="20"></td>
        <td><input type="number" class="progress-input" placeholder="0-100"><div class="progress-bar-container"><div class="progress-bar"></div></div><div class="calendar"></div></td>
        <td><input type="text" class="rating-input" placeholder="输入评级" size="20"></td>
      </tr>
      <tr>
        <td>调整作息</td>
        <td><input type="checkbox"></td>
        <td><input type="text" class="comment-input" placeholder="添加注释" size="20"></td>
        <td><input type="number" class="progress-input" placeholder="0-100"><div class="progress-bar-container"><div class="progress-bar"></div></div><div class="calendar"></div></td>
        <td><input type="text" class="rating-input" placeholder="输入评级" size="20"></td>
      </tr>
    </tbody>
  </table>
</div>