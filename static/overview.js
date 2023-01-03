let curhardfull = false;

setInterval(() => {
  $.get("/api1", function (data) {
    let mydata=myArr = JSON.parse(data);
    let temp=mydata["temp"];
    let freq=mydata["freq"];
    let usage=mydata["usage"];
    let mem=mydata["mem"];
    let uptime=mydata["uptime"];

    document.querySelector("#data-temp .value").innerHTML=temp;
    document.querySelector("#data-mem .value").innerHTML=mem;
    document.querySelector("#data-freq .value").innerHTML=freq;
    document.querySelector("#data-usage .value").innerHTML=usage;
    document.querySelector("#data-up .value").innerHTML=uptime;

  });
}, 1000);

document.querySelector(".showmore").addEventListener("click", (e) => {
  if (curhardfull == false) {
    let alltr = document.querySelectorAll(".hardware-data tr");
    for (var i = 6; i < alltr.length; i++) {
      alltr[i].style.display = "table-row";
    }
    document.querySelector(".showmore").innerHTML = "Show Less";
    curhardfull = true;
  } else {
    let alltr = document.querySelectorAll(".hardware-data tr");
    for (var i = 6; i < alltr.length; i++) {
      alltr[i].style.display = "none";
    }
    document.querySelector(".showmore").innerHTML = "Show more";
    curhardfull = false;
  }
});
