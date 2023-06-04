let nev = false;
let curhardfull = false;
let text_color = "#d8dee9";
if (current_theme == undefined) {
    current_theme = localStorage.getItem("current-theme");
}

if (current_theme == null) {
    localStorage.setItem("current-theme", "light");
    current_theme = "dark";
}

if (document.querySelector(".sidebar").clientWidth <= 60) {
    document.querySelector(".sidebar .sidecon i").style.display = "flex";
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

    document.querySelector(".sidebar .sidecon i").style.display = "none";

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
        r.style.setProperty("--mob-nev-ul-a-marginleft", "15px");
        r.style.setProperty("--mob-nev-ul-a-span", "inline");
        r.style.setProperty("--mob-nev-ul-i-marginright", "15px");
        r.style.setProperty("--mob-hrs", "none");
    }, 200);
}

function close_nev() {
    nev = false;

    document.querySelector(".sidebar .sidecon i").style.display = "flex";
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

try {
    document.querySelector("#control-center-btn").addEventListener("click", (e) => {
        document
            .querySelector("#control-center-btn")
            .classList.toggle("control-c-btn");
        document.querySelector(".control-center").classList.toggle("cc-open");
        console.log("cc");
        cc_state = true;
    });

} catch (error) {

}



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
        $.get("/savetheme", { theme: "light" });
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
        $.get("/savetheme", { theme: "dark" });
        text_color = "#d8dee9";
        if (!nev && document.querySelector(".sidebar").clientWidth <= 60) {
            // document.getElementById("expandbar").style.filter = "invert(180)";
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

// document.querySelector(".showmore").addEventListener("click", (e) => {
//     if (curhardfull == false) {
//         let alltr = document.querySelectorAll(".hardware-data tr");
//         for (var i = 6; i < alltr.length; i++) {
//             alltr[i].style.display = "table-row";
//         }
//         document.querySelector(".showmore").innerHTML = "Show Less";
//         curhardfull = true;
//     }
//     else {
//         let alltr = document.querySelectorAll(".hardware-data tr");
//         for (var i = 6; i < alltr.length; i++) {
//             alltr[i].style.display = "none";
//         }
//         document.querySelector(".showmore").innerHTML = "Show more";
//         curhardfull = false;
//     }

//     console.log(alltr.length);
// });
