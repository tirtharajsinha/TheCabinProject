let nev = false;

let text_color = "#d8dee9";
current_theme = localStorage.getItem("current-theme");
if (current_theme == null) {
  localStorage.setItem("current-theme", "dark");
  current_theme = "dark";
}



if (document.querySelector(".sidebar").clientWidth <= 60) {
  document.getElementById("expandbar").src = "right_arrow.png";
  if (current_theme == "dark") {
    document.getElementById("expandbar").style.filter = "invert(180)";
  }
}

if (current_theme == "light") {
  text_color = "#3b4252";
  document.body.classList.toggle("light-theme");
  // myChart.config.options.scales.x.ticks.color = "#3b4252";
  // myChart.config.options.scales.y.ticks.color = "#3b4252";
  // gaugechart.title.update({
  //   text: "Activity",
  //   style: {
  //     fontSize: "20px",
  //     color: text_color,
  //   },
  // });
  document.querySelector("#theme-toggle").classList.toggle("fa-moon");
  document.querySelector("#theme-toggle").classList.toggle("fa-sun");
} else {
  // myChart.config.options.scales.x.ticks.color = "#3b4252";
  // myChart.config.options.scales.y.ticks.color = "#3b4252";
  // gaugechart.title.update({
  //   text: "Activity",
  //   style: {
  //     fontSize: "20px",
  //     color: text_color,
  //   },
  // });
}

function open_nev() {
  nev = true;

  var r = document.querySelector(":root");
  r.style.setProperty("--mob-nev", "250px");

  document.getElementById("expandbar").src = "favicon.png";
  document.getElementById("expandbar").style.filter = "invert(0)";
  document.querySelector(".pagename").classList.toggle("fulld");
  document.querySelector(".pagetype").classList.toggle("fulld");
  document.querySelector(".close-nav-btn").style.display = "flex";

  setTimeout(() => {
    r.style.setProperty("--mob-brand-img", "50px");
    r.style.setProperty("--mob-nev-ul-width", "calc(100% - 10px)");
    r.style.setProperty("--mob-nev-ul-padding", "10px");
    r.style.setProperty("--mob-nev-ul-marginleft", "20px");
    r.style.setProperty("--mob-nev-ul-margin", "auto");
    r.style.setProperty("--mob-nev-ul-h3", "block");
    r.style.setProperty("--mob-nev-ul-a-marginleft", "25px");
    r.style.setProperty("--mob-nev-ul-a-span", "inline");
    r.style.setProperty("--mob-nev-ul-i-marginright", "20px");
    r.style.setProperty("--mob-hrs", "none");
  }, 200);
}

function close_nev() {
  nev = false;

  document.getElementById("expandbar").src = "right_arrow.png";
  if (current_theme == "dark") {
    document.getElementById("expandbar").style.filter = "invert(180)";
  }
  document.querySelector(".pagename").classList.toggle("fulld");
  document.querySelector(".pagetype").classList.toggle("fulld");
  document.querySelector(".close-nav-btn").style.display = "none";
  var r = document.querySelector(":root");
  r.style.setProperty("--mob-nev", "60px");
  r.style.setProperty("--mob-nev-ul-width", "100%");
  r.style.setProperty("--mob-nev-ul-padding", "0px");
  r.style.setProperty("--mob-brand-img", "30px");
  r.style.setProperty("--mob-nev-ul-marginleft", "0px");
  r.style.setProperty("--mob-nev-ul-margin", "auto");
  r.style.setProperty("--mob-nev-ul-h3", "none");
  r.style.setProperty("--mob-nev-ul-a-marginleft", "15px");
  r.style.setProperty("--mob-nev-ul-a-span", "none");
  r.style.setProperty("--mob-nev-ul-i-marginright", "0px");
  r.style.setProperty("--mob-hrs", "block");
}
document.getElementById("expandbar").addEventListener("click", (e) => {
  if (document.querySelector(".sidebar").clientWidth <= 60) {
    open_nev();
  } else if (nev) {
    close_nev();
  }
});

document.querySelector(".container").addEventListener("click", (e) => {
  if (nev) {
    close_nev();
  }
});

document.querySelector(".close-nav-btn").addEventListener("click", (e) => {
  if (nev) {
    close_nev();
  }
});

let cc_state = false;

document.querySelector("#control-center-btn").addEventListener("click", (e) => {
  document
    .querySelector("#control-center-btn")
    .classList.toggle("control-c-btn");
  document.querySelector(".control-center").classList.toggle("cc-open");
  console.log("cc");
  cc_state = true;
});

$(document).on("click", function (e) {
  var container = document.querySelector(".control-center");
  var btn = document.querySelector("#control-center-btn");

  if (
    !$(e.target).closest(container).length &&
    !$(e.target).closest(btn).length &&
    cc_state
  ) {
    document
      .querySelector("#control-center-btn")
      .classList.remove("control-c-btn");
    document.querySelector(".control-center").classList.remove("cc-open");
  }
});

document.querySelector("#theme-toggle").addEventListener("click", (e) => {
  show_loader();
  if (current_theme == "dark") {
    current_theme = "light";
    text_color = "#3b4252";
    if (!nev && document.querySelector(".sidebar").clientWidth <= 60) {
      document.getElementById("expandbar").style.filter = "invert(0)";
    }
    // myChart.config.options.scales.x.ticks.color = "#3b4252";
    // myChart.config.options.scales.y.ticks.color = "#3b4252";
    // gaugechart.title.update({
    //   text: "Activity",
    //   style: {
    //     fontSize: "20px",
    //     color: text_color,
    //   },
    // });
  } else {
    current_theme = "dark";
    text_color = "#d8dee9";
    if (!nev && document.querySelector(".sidebar").clientWidth <= 60) {
      document.getElementById("expandbar").style.filter = "invert(180)";
    }
    // myChart.config.options.scales.x.ticks.color = "#d8dee9";
    // myChart.config.options.scales.y.ticks.color = "#d8dee9";
    // gaugechart.title.update({
    //   text: "Activity",
    //   style: {
    //     fontSize: "20px",
    //     color: text_color,
    //   },
    // });
  }
  // myChart.update();
  document.body.classList.toggle("light-theme");
  document.querySelector("#theme-toggle").classList.toggle("fa-moon");
  document.querySelector("#theme-toggle").classList.toggle("fa-sun");
  localStorage.setItem("current-theme", current_theme);
});

function show_loader() {
  if (current_theme == "dark") {
    // document.querySelector(".ani-box").style.transform="scaleX(-1)";
  }
  document.querySelector(".theme-loader").style.display = "flex";
  document.querySelector(".ani-box").classList.add("change_theme");
  document.querySelector(".exp-box").classList.add("exp-expand");

  setTimeout(() => {
    document.querySelector(".theme-loader").style.display = "none";
    document.querySelector(".exp-box").classList.remove("exp-expand");
  }, 1120);

  setTimeout(() => {
    document.querySelector(".ani-box").classList.remove("change_theme");
  }, 1200);
}


$.get("/api4", function (data) {
  // let mydata=JSON.parse(data);
  console.log(data);
  let hostname = data["hostname"]
  let username = data["username"]

  let allhost = document.querySelectorAll(".data-hostname");
  for (var i = 0; i < allhost.length; i++) {
    allhost[i].innerHTML = hostname;
  }

  let alluser = document.querySelectorAll(".data-username");
  for (var i = 0; i < alluser.length; i++) {
    alluser[i].innerHTML = username;
  }


});

document.querySelector(".reconbtn").addEventListener("click", (e) => {
  location.reload();
})

setInterval(() => {
  try{
    $.get("/check", function (data) {
    }).fail(function () {
      
    })
  }
  catch{
    document.querySelector(".reconnect").style.display = "flex";
  }
}, 1000);

function reboot(){
  document.querySelector(".passbox .data-command").innerHTML = "Enter sudo password to reboot";
  document.querySelector(".passbox .passbtn").setAttribute('data-action',"reboot");
  document.querySelector(".passbox").style.display = "flex";
}

function poweroff(){
  document.querySelector(".passbox .data-command").innerHTML = "Enter sudo password to poweroff";
  document.querySelector(".passbox .passbtn").setAttribute('data-action',"poweroff");
  document.querySelector(".passbox").style.display = "flex";
}


document.querySelector(".cancelbtn").addEventListener("click", (e) => {
  document.querySelector(".passbox").style.display = "none";
  document.querySelector(".passdata").value = "";
})
$.ajaxSetup({ 
  beforeSend: function(xhr, settings) {
      function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
              var cookies = document.cookie.split(';');
              for (var i = 0; i < cookies.length; i++) {
                  var cookie = jQuery.trim(cookies[i]);
                  // Does this cookie string begin with the name we want?
                  if (cookie.substring(0, name.length + 1) == (name + '=')) {
                      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                      break;
                  }
              }
          }
          return cookieValue;
      }
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
          // Only send the token to relative URLs i.e. locally.
          xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
  } 
});

document.querySelector(".passbtn").addEventListener("click", (e) => {
  let pass = document.querySelector(".passdata").value;
  console.log(pass);
  let action=document.querySelector(".passbox .passbtn").getAttribute('data-action');
  let token = $("#change_password-form").find('input[name=csrfmiddlewaretoken]').val()
  document.querySelector(".passdata").value = "";
  document.querySelector(".passbox").style.display = "none";
  $.post(`/${action}`,
    {
      "sudopass": pass,
      "csrfmiddlewaretoken": token
    });

})