 // Function to hide alert messages after 5 seconds
 setTimeout(function () {
    var messages = document.querySelectorAll(".alert-message");
    messages.forEach(function (message) {
      message.style.opacity = "0";
      setTimeout(function () {
        message.style.display = "none";
      }, 1000);
    });
  }, 3000); // 5000 milliseconds = 5 seconds