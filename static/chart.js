// /**
//  * In the chart render event, add icons on top of the circular shapes
//  */
// function renderIcons() {
//   // Move icon
//   if (!this.series[0].icon) {
//     this.series[0].icon = this.renderer
//       .path(["M", -8, 0, "L", 8, 0, "M", 0, -8, "L", 8, 0, 0, 8])
//       .attr({
//         stroke: "#303030",
//         "stroke-linecap": "round",
//         "stroke-linejoin": "round",
//         "stroke-width": 2,
//         zIndex: 10,
//       })
//       .add(this.series[2].group);
//   }
//   this.series[0].icon.translate(
//     this.chartWidth / 2 - 10,
//     this.plotHeight / 2 -
//       this.series[0].points[0].shapeArgs.innerR -
//       (this.series[0].points[0].shapeArgs.r -
//         this.series[0].points[0].shapeArgs.innerR) /
//         2
//   );

//   // Exercise icon
//   if (!this.series[1].icon) {
//     this.series[1].icon = this.renderer
//       .path([
//         "M",
//         -8,
//         0,
//         "L",
//         8,
//         0,
//         "M",
//         0,
//         -8,
//         "L",
//         8,
//         0,
//         0,
//         8,
//         "M",
//         8,
//         -8,
//         "L",
//         16,
//         0,
//         8,
//         8,
//       ])
//       .attr({
//         stroke: "#ffffff",
//         "stroke-linecap": "round",
//         "stroke-linejoin": "round",
//         "stroke-width": 2,
//         zIndex: 10,
//       })
//       .add(this.series[2].group);
//   }
//   this.series[1].icon.translate(
//     this.chartWidth / 2 - 10,
//     this.plotHeight / 2 -
//       this.series[1].points[0].shapeArgs.innerR -
//       (this.series[1].points[0].shapeArgs.r -
//         this.series[1].points[0].shapeArgs.innerR) /
//         2
//   );

//   // Stand icon
//   if (!this.series[2].icon) {
//     this.series[2].icon = this.renderer
//       .path(["M", 0, 8, "L", 0, -8, "M", -8, 0, "L", 0, -8, 8, 0])
//       .attr({
//         stroke: "#303030",
//         "stroke-linecap": "round",
//         "stroke-linejoin": "round",
//         "stroke-width": 2,
//         zIndex: 10,
//       })
//       .add(this.series[2].group);
//   }

//   this.series[2].icon.translate(
//     this.chartWidth / 2 - 10,
//     this.plotHeight / 2 -
//       this.series[2].points[0].shapeArgs.innerR -
//       (this.series[2].points[0].shapeArgs.r -
//         this.series[2].points[0].shapeArgs.innerR) /
//         2
//   );
// }

// let gaugechart=new Highcharts.chart("gaugechart", {
//   chart: {
//     type: "solidgauge",
//     height: "100%",
//     events: {
//       render: renderIcons,
//     },
//     backgroundColor: "#00000000",
//   },

//   title: {
//     text: "Activity",
//     style: {
//       fontSize: "20px",
//       color: "#d8dee9",
//     },
//   },

//   tooltip: {
//     borderWidth: 0,
//     backgroundColor: "none",
//     shadow: false,
//     style: {
//       fontSize: "16px",
//     },
//     valueSuffix: "%",
//     pointFormat:
//       '<span class="gauge-title">{series.name}</span><br><span style="font-size:1.5em; color: {point.color}; font-weight: bold">{point.y}</span>',
//     positioner: function (labelWidth) {
//       return {
//         x: (this.chart.chartWidth - labelWidth) / 2,
//         y: this.chart.plotHeight / 2 + 20,
//       };
//     },
//   },
//   exporting: {
//     enabled: false,
//   },
//   credits: {
//     enabled: false,
//   },
//   pane: {
//     startAngle: 0,
//     endAngle: 360,
//     background: [
//       {
//         // Track for Move
//         outerRadius: "112%",
//         innerRadius: "88%",
//         backgroundColor: Highcharts.color(Highcharts.getOptions().colors[0])
//           .setOpacity(0.3)
//           .get(),
//         borderWidth: 0,
//       },
//       {
//         // Track for Exercise
//         outerRadius: "87%",
//         innerRadius: "63%",
//         backgroundColor: Highcharts.color(Highcharts.getOptions().colors[1])
//           .setOpacity(0.3)
//           .get(),
//         borderWidth: 0,
//       },
//       {
//         // Track for Stand
//         outerRadius: "62%",
//         innerRadius: "38%",
//         backgroundColor: Highcharts.color(Highcharts.getOptions().colors[2])
//           .setOpacity(0.3)
//           .get(),
//         borderWidth: 0,
//       },
//     ],
//   },

//   yAxis: {
//     min: 0,
//     max: 100,
//     lineWidth: 0,
//     tickPositions: [],
//   },

//   plotOptions: {
//     solidgauge: {
//       dataLabels: {
//         enabled: false,
//       },
//       linecap: "round",
//       stickyTracking: false,
//       rounded: true,
//     },
//   },

//   series: [
//     {
//       name: "Move",
//       data: [
//         {
//           color: "#88c0d0",
//           radius: "112%",
//           innerRadius: "88%",
//           y: 80,
//         },
//       ],
//     },
//     {
//       name: "Exercise",
//       data: [
//         {
//           color: "#5e81ac",
//           radius: "87%",
//           innerRadius: "63%",
//           y: 65,
//         },
//       ],
//     },
//     {
//       name: "Stand",
//       data: [
//         {
//           color: "#a3be8c",
//           radius: "62%",
//           innerRadius: "38%",
//           y: 50,
//         },
//       ],
//     },
//   ],
// });

// /*
// line chart for action density of tables


// */

// const ctx = document.getElementById("linechart").getContext("2d");

// const labels = ["January", "February", "March", "April", "May", "June"];

// const data = {
//   labels: labels,
//   datasets: [
//     {
//       label: "Event monitor",
//       backgroundColor: "#00000000",
//       borderColor: "#8fbcbb",
//       data: [0, 10, 5, 2, 20, 30, 45],
//       tension: 0.1,
//       borderWidth: 3,
//       pointStyle: "circle",
//       radius: 3,
//     },
//   ],
// };


// let current_theme="dark"
// let chart_color="#d8dee9";

// let config = {
//   responsive: true,
//   type: "line",
//   data: data,
//   options: {
//     scales: {
//       x: {
//         grid: {
//           display: false,
//         },
//         ticks: {
//           color: chart_color,
//         },
//       },
//       y: {
//         grid: {
//           display: false,
//         },
//         ticks: {
//           color: chart_color,
//         },
//       },
      
//     },
//   },
// };

// let myChart = new Chart(document.getElementById("linechart"), config);
// myChart.update();

