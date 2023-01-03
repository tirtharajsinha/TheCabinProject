let curhardfull = false;

setInterval(() => {
  $.get("/api1", function (data) {
    // let mydata=JSON.parse(data);
    
    let temp=data["temp"];
    let freq=data["freq"];
    let usage=data["usage"];
    let mem=data["mem"];
    let uptime=data["uptime"];

    document.querySelector("#data-temp .value").innerHTML=temp;
    document.querySelector("#data-mem .value").innerHTML=mem;
    document.querySelector("#data-freq .value").innerHTML=freq;
    document.querySelector("#data-usage .value").innerHTML=usage;
    document.querySelector("#data-up .value").innerHTML=uptime;

  });
}, 1000);

$.get("/api2", function (data) {
  // let mydata=JSON.parse(data);
  
  let sto=data["storage"];
  let Tser=data["totalservices"];
  let Fser=data["failedservice"];

  document.querySelector("#data-sto .value").innerHTML=sto;
  document.querySelector("#data-service .value").innerHTML=Tser;
  document.querySelector("#data-fail .value").innerHTML=Fser;
  

});
setInterval(() => {
  $.get("/api3", function (data) {
    // let mydata=JSON.parse(data);
    
    let core1=data["core1"];
    let core2=data["core2"];
    let core3=data["core3"];
    let core4=data["core4"];
    let allcore=(core1+core2+core3+core4)/4;
    
    document.querySelector(".core1").style.width=Math.round(core1)+"%";
    document.querySelector(".core1 .cdata").innerHTML=core1+"%";

    document.querySelector(".core2").style.width=Math.round(core2)+"%";
    document.querySelector(".core2 .cdata").innerHTML=core2+"%";

    document.querySelector(".core3").style.width=Math.round(core3)+"%";
    document.querySelector(".core3 .cdata").innerHTML=core3+"%";

    document.querySelector(".core4").style.width=Math.round(core4)+"%";
    document.querySelector(".core4 .cdata").innerHTML=core4+"%";

    document.querySelector(".allcore").style.width=Math.round(allcore)+"%";
    document.querySelector(".allcore .cdata").innerHTML=allcore.toFixed(1)+"%";


  });
}, 100);

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
