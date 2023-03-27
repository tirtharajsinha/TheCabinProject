let curhardfull = false;



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
