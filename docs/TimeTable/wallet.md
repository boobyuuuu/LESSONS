<style>
  /* 基于calendar.md的主题风格 */
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
  h1 {
    font-weight: bold;
    text-align: center;
    font-size: 2.5em;
    padding: 10px;
    border-radius: 8px;
  }
  .section-title {
    text-align: center;
    font-size: 1.6em;
    background-color: #ffc7c7;
    padding: 10px;
    border-radius: 8px;
    margin-top: 40px; /* 增加距离 */
    margin-bottom: 20px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
  }
  th {
    background-color: #ffe2e2;
  }
  button {
    background-color: #ffe2e2;
    color: black;
    padding: 10px 10px;
    border: none;
    border-radius: 1px;
    cursor: pointer;
    font-size: 1em;
  }
  button:hover {
    background-color: #f6f6f6;
  }
  .form-group {
    margin-bottom: 15px;
  }
  input[type="text"], input[type="number"], input[type="datetime-local"], select {
    width: 60%;
    padding: 8px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: 'xiaokai', sans-serif;
    transition: border-color 0.3s, box-shadow 0.3s;
  }
  input[type="text"]:focus, input[type="number"]:focus, input[type="datetime-local"]:focus, select:focus {
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
  .summary-info {
    font-size: 1.2em;
    margin-bottom: 20px;
  }
  .transaction-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .transaction-card h4 {
    margin: 0 0 10px 0;
  }
  .transaction-card p {
    margin: 5px 0;
  }
</style>

<script>
  let accounts = JSON.parse(localStorage.getItem('accounts')) || {};

  document.addEventListener('DOMContentLoaded', () => {
    const transactionAccountSelect = document.getElementById('transaction-account-select');
    const summaryAccountSelect = document.getElementById('summary-account-select');
    const exportAccountSelect = document.getElementById('export-account-select');
    const deleteAccountSelect = document.getElementById('delete-account-select');
    const transactionDate = document.getElementById('transaction-date');
    const startDate = document.getElementById('start-date');
    const endDate = document.getElementById('end-date');
    const transactionType = document.getElementById('transaction-type');
    const incomeTypeContainer = document.getElementById('income-type-container');
    const expenseTypeContainer = document.getElementById('expense-type-container');
    const subExpenseTypeContainer = document.getElementById('sub-expense-type-container');
    const expenseType = document.getElementById('expense-type');

    const today = new Date().toISOString().slice(0, 16);
    transactionDate.value = today;
    startDate.value = new Date().toISOString().slice(0, 10);
    endDate.value = new Date().toISOString().slice(0, 10);

    for (const account in accounts) {
      const option = document.createElement('option');
      option.value = account;
      option.text = account;
      transactionAccountSelect.add(option.cloneNode(true));
      summaryAccountSelect.add(option.cloneNode(true));
      exportAccountSelect.add(option.cloneNode(true));
      deleteAccountSelect.add(option.cloneNode(true));
    }

    transactionType.addEventListener('change', () => {
      if (transactionType.value === 'deposit') {
        incomeTypeContainer.style.display = 'block';
        expenseTypeContainer.style.display = 'none';
        subExpenseTypeContainer.style.display = 'none';
      } else if (transactionType.value === 'withdraw') {
        incomeTypeContainer.style.display = 'none';
        expenseTypeContainer.style.display = 'block';
        if (expenseType.value === '生活支出') {
          subExpenseTypeContainer.style.display = 'block';
        } else {
          subExpenseTypeContainer.style.display = 'none';
        }
      } else {
        incomeTypeContainer.style.display = 'none';
        expenseTypeContainer.style.display = 'none';
        subExpenseTypeContainer.style.display = 'none';
      }
    });

    expenseType.addEventListener('change', () => {
      if (expenseType.value === '生活支出') {
        subExpenseTypeContainer.style.display = 'block';
      } else {
        subExpenseTypeContainer.style.display = 'none';
      }
    });
  });

  function addAccount() {
    const accountName = document.getElementById('account-name').value;
    if (accountName && !accounts[accountName]) {
      accounts[accountName] = { balance: 0, transactions: [] };
      localStorage.setItem('accounts', JSON.stringify(accounts));
      const transactionAccountSelect = document.getElementById('transaction-account-select');
      const summaryAccountSelect = document.getElementById('summary-account-select');
      const exportAccountSelect = document.getElementById('export-account-select');
      const deleteAccountSelect = document.getElementById('delete-account-select');
      const option = document.createElement('option');
      option.value = accountName;
      option.text = accountName;
      transactionAccountSelect.add(option.cloneNode(true));
      summaryAccountSelect.add(option.cloneNode(true));
      exportAccountSelect.add(option.cloneNode(true));
      deleteAccountSelect.add(option.cloneNode(true));
      alert('账户添加成功');
    } else {
      alert('账户名称不能为空或已存在');
    }
  }

  function deleteAccount() {
    const deleteAccountSelect = document.getElementById('delete-account-select');
    const selectedAccount = deleteAccountSelect.value;
    if (selectedAccount) {
      delete accounts[selectedAccount];
      localStorage.setItem('accounts', JSON.stringify(accounts));
      location.reload();
      alert('账户删除成功');
    } else {
      alert('请选择一个账户');
    }
  }

  function checkBalance() {
    const transactionAccountSelect = document.getElementById('transaction-account-select');
    const selectedAccount = transactionAccountSelect.value;
    if (selectedAccount) {
      const balance = accounts[selectedAccount]?.balance ?? 0;
      document.getElementById('balance-result').innerText = `账户余额: ${balance} 元`;
    } else {
      alert('请选择一个账户');
    }
  }

  function performTransaction() {
    const transactionAccountSelect = document.getElementById('transaction-account-select');
    const selectedAccount = transactionAccountSelect.value;
    const amount = parseFloat(document.getElementById('transaction-amount').value);
    const type = document.getElementById('transaction-type').value;
    const note = document.getElementById('transaction-note').value;
    const date = new Date(document.getElementById('transaction-date').value).toLocaleString();
    const incomeType = document.getElementById('income-type').value;
    const expenseType = document.getElementById('expense-type').value;
    const subExpenseType = document.getElementById('sub-expense-type').value;

    if (selectedAccount && amount > 0) {
      let transactionDetail = '';
      if (type === 'deposit') {
        accounts[selectedAccount].balance += amount;
        accounts[selectedAccount].transactions.push({ type, amount, note, date, incomeType });
        transactionDetail = `存入 - ${incomeType}`;
      } else if (type === 'withdraw') {
        accounts[selectedAccount].balance -= amount;
        accounts[selectedAccount].transactions.push({ type, amount, note, date, expenseType, subExpenseType });
        transactionDetail = `支出 - ${expenseType}${subExpenseType ? ' - ' + subExpenseType : ''}`;
      }
      localStorage.setItem('accounts', JSON.stringify(accounts));
      alert(`操作成功: ${transactionDetail} ${amount} 元\n备注: ${note}\n时间: ${date}`);
      checkBalance();
    } else {
      alert('请选择一个账户并输入有效金额');
    }
  }

  function showSummary() {
    const summaryAccountSelect = document.getElementById('summary-account-select');
    const selectedAccount = summaryAccountSelect.value;
    const startDate = new Date(document.getElementById('start-date').value);
    const endDate = new Date(document.getElementById('end-date').value);
    const summaryResult = document.getElementById('summary-result');

    if (selectedAccount && startDate && endDate) {
      const accountTransactions = accounts[selectedAccount].transactions;
      const filteredTransactions = accountTransactions.filter(transaction => {
        const transactionDate = new Date(transaction.date);
        return transactionDate >= startDate && transactionDate <= endDate;
      });

      filteredTransactions.sort((a, b) => new Date(a.date) - new Date(b.date));

      const totalIncome = filteredTransactions
        .filter(transaction => transaction.type === 'deposit')
        .reduce((sum, transaction) => sum + transaction.amount, 0);
      const totalExpense = filteredTransactions
        .filter(transaction => transaction.type === 'withdraw')
        .reduce((sum, transaction) => sum + transaction.amount, 0);

      let summaryHtml = `<div class="summary-info">交易笔数: ${filteredTransactions.length}, 收入总数: ${totalIncome} 元, 支出总数: ${totalExpense} 元</div>`;
      filteredTransactions.forEach(transaction => {
        summaryHtml += `
          <div class="transaction-card">
            <h4>${transaction.date}</h4>
            <p>类型: ${transaction.type === 'deposit' ? `存入 - ${transaction.incomeType}` : `支出 - ${transaction.expenseType}${transaction.subExpenseType ? ' - ' + transaction.subExpenseType : ''}`}</p>
            <p>金额: ${transaction.amount} 元</p>
            <p>备注: ${transaction.note}</p>
          </div>
        `;
      });

      summaryResult.innerHTML = summaryHtml;
    } else {
      alert('请选择一个账户并输入有效的日期范围');
    }
  }

  function showTodaySummary() {
    const summaryAccountSelect = document.getElementById('summary-account-select');
    const selectedAccount = summaryAccountSelect.value;
    const today = new Date();
    const startDate = new Date(today.setDate(today.getDate() - 1));
    const endDate = new Date(today.setDate(today.getDate() + 2));
    const summaryResult = document.getElementById('summary-result');

    if (selectedAccount) {
      const accountTransactions = accounts[selectedAccount].transactions;
      const filteredTransactions = accountTransactions.filter(transaction => {
        const transactionDate = new Date(transaction.date);
        return transactionDate >= startDate && transactionDate <= endDate;
      });

      filteredTransactions.sort((a, b) => new Date(a.date) - new Date(b.date));

      const totalIncome = filteredTransactions
        .filter(transaction => transaction.type === 'deposit')
        .reduce((sum, transaction) => sum + transaction.amount, 0);
      const totalExpense = filteredTransactions
        .filter(transaction => transaction.type === 'withdraw')
        .reduce((sum, transaction) => sum + transaction.amount, 0);

      let summaryHtml = `<div class="summary-info">交易笔数: ${filteredTransactions.length}, 收入总数: ${totalIncome} 元, 支出总数: ${totalExpense} 元</div>`;
      filteredTransactions.forEach(transaction => {
        summaryHtml += `
          <div class="transaction-card">
            <h4>${transaction.date}</h4>
            <p>类型: ${transaction.type === 'deposit' ? `存入 - ${transaction.incomeType}` : `支出 - ${transaction.expenseType}${transaction.subExpenseType ? ' - ' + transaction.subExpenseType : ''}`}</p>
            <p>金额: ${transaction.amount} 元</p>
            <p>备注: ${transaction.note}</p>
          </div>
        `;
      });

      summaryResult.innerHTML = summaryHtml;
    } else {
      alert('请选择一个账户');
    }
  }

  function showWeekSummary() {
    const summaryAccountSelect = document.getElementById('summary-account-select');
    const selectedAccount = summaryAccountSelect.value;
    const today = new Date();
    const startDate = new Date(today.setDate(today.getDate() - today.getDay()));
    const endDate = new Date(today.setDate(today.getDate() + 7));
    const summaryResult = document.getElementById('summary-result');

    if (selectedAccount) {
      const accountTransactions = accounts[selectedAccount].transactions;
      const filteredTransactions = accountTransactions.filter(transaction => {
        const transactionDate = new Date(transaction.date);
        return transactionDate >= startDate && transactionDate <= endDate;
      });

      filteredTransactions.sort((a, b) => new Date(a.date) - new Date(b.date));

      const totalIncome = filteredTransactions
        .filter(transaction => transaction.type === 'deposit')
        .reduce((sum, transaction) => sum + transaction.amount, 0);
      const totalExpense = filteredTransactions
        .filter(transaction => transaction.type === 'withdraw')
        .reduce((sum, transaction) => sum + transaction.amount, 0);

      let summaryHtml = `<div class="summary-info">交易笔数: ${filteredTransactions.length}, 收入总数: ${totalIncome} 元, 支出总数: ${totalExpense} 元</div>`;
      filteredTransactions.forEach(transaction => {
        summaryHtml += `
          <div class="transaction-card">
            <h4>${transaction.date}</h4>
            <p>类型: ${transaction.type === 'deposit' ? `存入 - ${transaction.incomeType}` : `支出 - ${transaction.expenseType}${transaction.subExpenseType ? ' - ' + transaction.subExpenseType : ''}`}</p>
            <p>金额: ${transaction.amount} 元</p>
            <p>备注: ${transaction.note}</p>
          </div>
        `;
      });

      summaryResult.innerHTML = summaryHtml;
    } else {
      alert('请选择一个账户');
    }
  }

  function showMonthSummary() {
    const summaryAccountSelect = document.getElementById('summary-account-select');
    const selectedAccount = summaryAccountSelect.value;
    const today = new Date();
    const startDate = new Date(today.getFullYear(), today.getMonth(), 1);
    const endDate = new Date(today.getFullYear(), today.getMonth() + 1, 0);
    const summaryResult = document.getElementById('summary-result');

    if (selectedAccount) {
      const accountTransactions = accounts[selectedAccount].transactions;
      const filteredTransactions = accountTransactions.filter(transaction => {
        const transactionDate = new Date(transaction.date);
        return transactionDate >= startDate && transactionDate <= endDate;
      });

      filteredTransactions.sort((a, b) => new Date(a.date) - new Date(b.date));

      const totalIncome = filteredTransactions
        .filter(transaction => transaction.type === 'deposit')
        .reduce((sum, transaction) => sum + transaction.amount, 0);
      const totalExpense = filteredTransactions
        .filter(transaction => transaction.type === 'withdraw')
        .reduce((sum, transaction) => sum + transaction.amount, 0);

      let summaryHtml = `<div class="summary-info">交易笔数: ${filteredTransactions.length}, 收入总数: ${totalIncome} 元, 支出总数: ${totalExpense} 元</div>`;
      filteredTransactions.forEach(transaction => {
        summaryHtml += `
          <div class="transaction-card">
            <h4>${transaction.date}</h4>
            <p>类型: ${transaction.type === 'deposit' ? `存入 - ${transaction.incomeType}` : `支出 - ${transaction.expenseType}${transaction.subExpenseType ? ' - ' + transaction.subExpenseType : ''}`}</p>
            <p>金额: ${transaction.amount} 元</p>
            <p>备注: ${transaction.note}</p>
          </div>
        `;
      });

      summaryResult.innerHTML = summaryHtml;
    } else {
      alert('请选择一个账户');
    }
  }

  function importAccounts() {
    const importFile = document.getElementById('import-file').files[0];
    if (importFile) {
      const reader = new FileReader();
      reader.onload = function(event) {
        const importedData = JSON.parse(event.target.result);
        accounts = { ...accounts, ...importedData };
        localStorage.setItem('accounts', JSON.stringify(accounts));
        location.reload();
      };
      reader.readAsText(importFile);
    } else {
      alert('请选择一个文件');
    }
  }

  function exportAccount() {
    const exportAccountSelect = document.getElementById('export-account-select');
    const selectedAccount = exportAccountSelect.value;
    if (selectedAccount) {
      const dataStr = JSON.stringify(accounts[selectedAccount]);
      const dataUri = 'data:application/json;charset=utf-8,' + encodeURIComponent(dataStr);
      const exportFileDefaultName = `${selectedAccount}.json`;
      const linkElement = document.createElement('a');
      linkElement.setAttribute('href', dataUri);
      linkElement.setAttribute('download', exportFileDefaultName);
      linkElement.click();
    } else {
      alert('请选择一个账户');
    }
  }
</script>

<div class="container">
  <h1>个人钱包管理器</h1>

  <div class="section-title">账户管理</div>
  <form id="account-form">
    <div class="form-group">
      <label for="account-name">账户名称:</label>
      <input type="text" id="account-name" name="account-name" required>
      <button type="button" onclick="addAccount()">添加账户</button>
    </div>
  </form>
  <form id="import-form">
    <div class="form-group">
      <label for="import-file">导入账户:</label>
      <input type="file" id="import-file" name="import-file" accept=".json">
      <button type="button" onclick="importAccounts()">导入</button>
    </div>
  </form>
  <div class="form-group">
    <label for="export-account-select">导出账户:</label>
    <select id="export-account-select" name="export-account-select"></select>
    <button type="button" onclick="exportAccount()">导出账户</button>
  </div>

  <div class="form-group">
    <label for="delete-account-select">删除账户:</label>
    <select id="delete-account-select" name="delete-account-select"></select>
    <button type="button" onclick="deleteAccount()">删除账户</button>
  </div>

  <div class="section-title">账户操作</div>
  <form id="transaction-form">
    <div class="form-group">
      <label for="transaction-account-select">账户:</label>
      <select id="transaction-account-select" name="transaction-account-select"></select>
      <button type="button" onclick="checkBalance()">查询余额</button>
    </div>
    <div id="balance-result"></div>
    <div class="form-group">
      <label for="transaction-amount">金额:</label>
      <input type="number" id="transaction-amount" name="transaction-amount" required>
    </div>
    <div class="form-group">
      <label for="transaction-type">类型:</label>
      <select id="transaction-type" name="transaction-type">
        <option value="deposit">存入</option>
        <option value="withdraw">支出</option>
      </select>
    </div>
    <div class="form-group" id="income-type-container" style="display: none;">
      <label for="income-type">存入类型:</label>
      <select id="income-type" name="income-type">
        <option value="固定收入">固定收入</option>
        <option value="临时收入">临时收入</option>
      </select>
    </div>
    <div class="form-group" id="expense-type-container" style="display: none;">
      <label for="expense-type">支出类型:</label>
      <select id="expense-type" name="expense-type">
        <option value="生活支出">生活支出</option>
        <option value="学习支出">学习支出</option>
        <option value="娱乐支出">娱乐支出</option>
      </select>
    </div>
    <div class="form-group" id="sub-expense-type-container" style="display: none;">
      <label for="sub-expense-type">生活支出类型:</label>
      <select id="sub-expense-type" name="sub-expense-type">
        <option value="衣">衣</option>
        <option value="食">食</option>
        <option value="住">住</option>
        <option value="行">行</option>
        <option value="社交">社交</option>
      </select>
    </div>
    <div class="form-group">
      <label for="transaction-note">备注:</label>
      <input type="text" id="transaction-note" name="transaction-note">
    </div>
    <div class="form-group">
      <label for="transaction-date">时间:</label>
      <input type="datetime-local" id="transaction-date" name="transaction-date" required>
    </div>
    <button type="button" onclick="performTransaction()">提交</button>
  </form>

  <div class="section-title">账户总结</div>
  <form id="summary-form">
    <div class="form-group">
      <label for="summary-account-select">选择账户:</label>
      <select id="summary-account-select" name="summary-account-select"></select>
    </div>
    <div class="form-group">
      <label for="start-date">开始日期:</label>
      <input type="date" id="start-date" name="start-date" required>
    </div>
    <div class="form-group">
      <label for="end-date">结束日期:</label>
      <input type="date" id="end-date" name="end-date" required>
    </div>
    <button type="button" onclick="showSummary()">显示总结</button>
    <button type="button" onclick="showTodaySummary()">显示今日明细</button>
    <button type="button" onclick="showWeekSummary()">显示本周明细</button>
    <button type="button" onclick="showMonthSummary()">显示本月明细</button>
  </form>
  
  <div id="summary-result"></div>
</div>