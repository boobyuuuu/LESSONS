# 密码保护文档

<div id="password-protected" style="text-align: center; margin-top: 50px;">
  <!-- <h2 style="font-family: 'Helvetica Neue', sans-serif; font-weight: 300; color: #333;">请输入密码</h2> -->
  <input type="password" id="password" style="padding: 10px; font-size: 16px; border: 1px solid #ccc; border-radius: 4px; width: 70%; max-width: 300px;" placeholder="请输入密码">
  <button onclick="checkPassword()" style="background-color: #0078d4; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; margin-top: 20px;">验证</button>
  <p id="error-message" style="color: red; display: none; margin-top: 20px; font-size: 14px;">密码错误，请重新输入。</p>
</div>

<div id="document-content" style="display: none; text-align: center; margin-top: 50px;">
  <h3 style="font-family: 'Helvetica Neue', sans-serif; font-weight: 300; color: #333;">欢迎访问文档内容</h3>
  <p style="font-family: 'Helvetica Neue', sans-serif; color: #555; line-height: 1.8; font-size: 18px; max-width: 800px; margin: 0 auto;">这是受密码保护的文档内容。只有输入正确密码后，您才能查看此内容。</p>
</div>

<!-- <div id="document-content" style="display: none;">
  {% include-markdown "content/protected_content.md" %}

  ## 骚话大全
</div> -->

<script>
  function checkPassword() {
    const correctPassword = "211840339"; // 设置密码
    const enteredPassword = document.getElementById("password").value;
    if (enteredPassword === correctPassword) {
      document.getElementById("password-protected").style.display = "none";
      document.getElementById("document-content").style.display = "block";
    } else {
      document.getElementById("error-message").style.display = "block";
    }
  }
</script>
