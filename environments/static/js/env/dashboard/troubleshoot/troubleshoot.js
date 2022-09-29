'use strict';

var ExAsTroubleShoot = (function() {
    var MAIN = 'dashboard';
    var e3nCeL0t = ExAs.uXvbI(uXvbI);
    var MoDaD = ExAs.m0d(m0d);
    var GlobalColor = ["#65A7E4", "#FD8839"]
    var ExecutionRateChart, DowntimeRatioChart, AvailableAccChart, mtbfChart, mttrChart, MekanicalChart, ElektricalChart

    var ExecutionRate = function() {
        var options,
            chartDonutBasicColors = GlobalColor;
        chartDonutBasicColors &&
            ((options = {
                    series: [0, 0],
                    labels: ["Executed", "Pending"],
                    chart: { height: 333, type: "pie" },
                    legend: { position: "bottom" },
                    stroke: { show: !1 },
                    dataLabels: { dropShadow: { enabled: !1 } },
                    colors: chartDonutBasicColors,
                }),
                (ExecutionRateChart = new ApexCharts(document.querySelector("#ExecutionRate"), options)).render());
    }

    var DowntimeRatio = function() {
        var options,
            chartDonutBasicColors = GlobalColor;
        chartDonutBasicColors &&
            ((options = {
                    series: [0, 0],
                    labels: ["Planned DT", "Unplanned DT"],
                    chart: { height: 333, type: "pie" },
                    legend: { position: "bottom" },
                    stroke: { show: !1 },
                    dataLabels: { dropShadow: { enabled: !1 } },
                    colors: chartDonutBasicColors,
                }),
                (DowntimeRatioChart = new ApexCharts(document.querySelector("#DowntimeRatio"), options)).render());
    }

    var AvailableAcc = function() {
        var linechartcustomerColors = GlobalColor
        linechartcustomerColors &&
            ((options = {
                    series: [
                        { name: "Availability (%)", type: "area", data: [34, 65, 46, 68, 49, 61, 42, 44, 78, 52, 63, 67] },
                        { name: "Target (%)", type: "area", data: [94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94] },
                    ],
                    chart: { height: 370, type: "line", toolbar: { show: !1 } },
                    stroke: { curve: "straight", dashArray: [0, 0], width: [2, 2] },
                    fill: { opacity: [0, 0] },
                    markers: { size: [0, 0], strokeWidth: 2, hover: { size: 4 } },
                    xaxis: { categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], axisTicks: { show: !1 }, axisBorder: { show: !1 } },
                    grid: { show: !0, xaxis: { lines: { show: !0 } }, yaxis: { lines: { show: !1 } }, padding: { top: 0, right: 8, bottom: 15, left: 8 } },
                    legend: { show: !0, horizontalAlign: "center", offsetX: 0, offsetY: -5, markers: { width: 9, height: 9, radius: 6 }, itemMargin: { horizontal: 10, vertical: 0 } },
                    plotOptions: { bar: { columnWidth: "30%", barHeight: "70%" } },
                    colors: linechartcustomerColors,
                    tooltip: {
                        shared: !0,
                        y: [{
                                formatter: function(e) {
                                    return void 0 !== e ? ": " + e.toFixed(2) : e;
                                },
                            },
                            {
                                formatter: function(e) {
                                    return void 0 !== e ? ": " + e.toFixed(2) : e;
                                },
                            },
                        ],
                    },
                }),
                (AvailableAccChart = new ApexCharts(document.querySelector("#AvailableAcc"), options)).render());
    }

    var MtbfChart = function() {
        var linechartcustomerColors = GlobalColor
        linechartcustomerColors &&
            ((options = {
                    series: [
                        { name: "Trouble Frequency", type: "bar", data: [89.25, 98.58, 68.74, 108.87, 77.54, 84.03, 51.24, 28.57, 92.57, 42.36, 88.51, 36.57] },
                        { name: "MTBF", type: "area", data: [8, 12, 7, 17, 21, 11, 5, 9, 7, 29, 12, 35] },
                    ],
                    chart: { height: 370, type: "line", toolbar: { show: !1 } },
                    stroke: { curve: "straight", dashArray: [0, 0], width: [2, 2] },
                    fill: { opacity: [1, 0] },
                    markers: { size: [0, 0], strokeWidth: 2, hover: { size: 4 } },
                    xaxis: { categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], axisTicks: { show: !1 }, axisBorder: { show: !1 } },
                    grid: { show: !0, xaxis: { lines: { show: !0 } }, yaxis: { lines: { show: !1 } }, padding: { top: 0, right: 8, bottom: 15, left: 10 } },
                    legend: { show: !0, horizontalAlign: "center", offsetX: 0, offsetY: -5, markers: { width: 9, height: 9, radius: 6 }, itemMargin: { horizontal: 10, vertical: 0 } },
                    plotOptions: { bar: { columnWidth: "30%", barHeight: "70%" } },
                    colors: linechartcustomerColors,
                    tooltip: {
                        shared: !0,
                        y: [{
                                formatter: function(e) {
                                    return void 0 !== e ? ": " + e.toFixed(2) : e;
                                },
                            },
                            {
                                formatter: function(e) {
                                    return void 0 !== e ? ": " + e.toFixed(2) : e;
                                },
                            },
                        ],
                    },
                }),
                (mtbfChart = new ApexCharts(document.querySelector("#MtbfChart"), options)).render());
    }

    var MttrChart = function() {
        var linechartcustomerColors = GlobalColor
        linechartcustomerColors &&
            ((options = {
                    series: [
                        { name: "MTTR", type: "area", data: [34, 65, 46, 68, 49, 61, 42, 44, 78, 52, 63, 67] },
                        { name: "Target", type: "area", data: [0, 45, 7, 17, 21, 11, 5, 0, 7, 29, 12, 35] },
                    ],
                    chart: { height: 370, type: "line", toolbar: { show: !1 } },
                    stroke: { curve: "straight", dashArray: [0, 0], width: [2, 2] },
                    fill: { opacity: [0, 0] },
                    markers: { size: [0, 0], strokeWidth: 2, hover: { size: 4 } },
                    xaxis: { categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], axisTicks: { show: !1 }, axisBorder: { show: !1 } },
                    grid: { show: !0, xaxis: { lines: { show: !0 } }, yaxis: { lines: { show: !1 } }, padding: { top: 0, right: 10, bottom: 15, left: 10 } },
                    legend: { show: !0, horizontalAlign: "center", offsetX: 0, offsetY: -5, markers: { width: 9, height: 9, radius: 6 }, itemMargin: { horizontal: 10, vertical: 0 } },
                    colors: linechartcustomerColors,
                    tooltip: {
                        shared: !0,
                        y: [{
                                formatter: function(e) {
                                    return void 0 !== e ? ": " + e.toFixed(2) : e;
                                },
                            },
                            {
                                formatter: function(e) {
                                    return void 0 !== e ? ": " + e.toFixed(2) : e;
                                },
                            },
                        ],
                    },
                }),
                (mttrChart = new ApexCharts(document.querySelector("#MttrChart"), options)).render());
    }

    var Mekanical = function() {
        var linechartcustomerColors = GlobalColor
        linechartcustomerColors &&
            ((options = {
                    series: [
                        { name: "Mekanikal", type: "bar", data: [34, 65, 46, 68, 49, 61, 42, 44, 78, 52, 63, 67] }
                    ],
                    chart: { height: 370, type: "line", toolbar: { show: !1 } },
                    stroke: { curve: "straight", dashArray: [0], width: [2] },
                    fill: { opacity: [1] },
                    markers: { size: [0], strokeWidth: 2, hover: { size: 4 } },
                    xaxis: { categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], axisTicks: { show: !1 }, axisBorder: { show: !1 } },
                    grid: { show: !0, xaxis: { lines: { show: !0 } }, yaxis: { lines: { show: !1 } }, padding: { top: 0, right: 10, bottom: 15, left: 10 } },
                    legend: { show: !0, horizontalAlign: "center", offsetX: 0, offsetY: -5, markers: { width: 9, height: 9, radius: 6 }, itemMargin: { horizontal: 10, vertical: 0 } },
                    colors: linechartcustomerColors,
                    tooltip: {
                        shared: !0,
                        y: [{
                            formatter: function(e) {
                                return void 0 !== e ? ": " + e.toFixed(0) : e;
                            },
                        }],
                    },
                }),
                (MekanicalChart = new ApexCharts(document.querySelector("#FrekMekaChart"), options)).render());
    }

    var Elektrical = function() {
        var linechartcustomerColors = GlobalColor
        linechartcustomerColors &&
            ((options = {
                    series: [
                        { name: "Elektrikal", type: "bar", data: [34, 65, 46, 68, 49, 61, 42, 44, 78, 52, 63, 67] }
                    ],
                    chart: { height: 370, type: "line", toolbar: { show: !1 } },
                    stroke: { curve: "straight", dashArray: [0], width: [2] },
                    fill: { opacity: [1] },
                    markers: { size: [0], strokeWidth: 2, hover: { size: 4 } },
                    xaxis: { categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], axisTicks: { show: !1 }, axisBorder: { show: !1 } },
                    grid: { show: !0, xaxis: { lines: { show: !0 } }, yaxis: { lines: { show: !1 } }, padding: { top: 0, right: 10, bottom: 15, left: 10 } },
                    legend: { show: !0, horizontalAlign: "center", offsetX: 0, offsetY: -5, markers: { width: 9, height: 9, radius: 6 }, itemMargin: { horizontal: 10, vertical: 0 } },
                    colors: linechartcustomerColors,
                    tooltip: {
                        shared: !0,
                        y: [{
                            formatter: function(e) {
                                return void 0 !== e ? ": " + e.toFixed(0) : e;
                            },
                        }],
                    },
                }),
                (ElektricalChart = new ApexCharts(document.querySelector("#FrekElekChart"), options)).render());
    }

    var loadData = function(start_date = '', end_date = '') {
        $('.full-loading').addClass('active')
        var ts = start_date,
            te = end_date
        $.ajax({
            url: e3nCeL0t + MoDaD + MAIN + "/load",
            method: "POST",
            async: false,
            data: {
                scrty: true,
                tgl_start: ts,
                tgl_end: te,
            },
            success: function(response) {
                $('.full-loading').removeClass('active')
                var respon = ExAs.uXvbI(response)
                if (ExAs.Utils.Json.valid(respon)) {
                    var res = JSON.parse(respon)
                    if (res.success) {
                        var grap = res.data

                        /**
                         * Execution Rate
                         */
                        var er = grap.execution_rate[0]
                        if (parseFloat(er.total_executed) === 0 && parseFloat(er.total_pending) === 0) {
                            $('#ExecutionRate').html('Belum Ada Data, Grafik Tidak Ditampilkan')
                        } else {
                            var era = [parseFloat(er.total_executed), parseFloat(er.total_pending)]
                                // ExecutionRate(era)
                            ExecutionRateChart.updateSeries(era)
                        }

                        /**
                         * Downtime Ratio
                         */
                        var dr = grap.downtime_ratio[0]
                        if (parseFloat(dr.planned_downtime) === 0 && parseFloat(dr.unplanned_downtime) === 0) {
                            $('#DowntimeRatio').html('Belum Ada Data, Grafik Tidak Ditampilkan')
                        } else {
                            var dra = [parseFloat(dr.planned_downtime), parseFloat(dr.unplanned_downtime)]
                            DowntimeRatioChart.updateSeries(dra)
                        }

                        /**
                         * Available ACC
                         */
                        var month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

                        var av = grap.availability
                        var dynTargetAvailability = [],
                            valTargetAvailability = 94,
                            dynCategories = [],
                            dynValue = []

                        var monthIndex = 0;
                        for (var i = 0; i < av.length; i++) {
                            var datVal = av[i]
                            dynTargetAvailability.push(valTargetAvailability)
                            dynCategories.push(month[monthIndex] + ' ' + datVal.tahun)
                            dynValue.push(datVal.value)
                            monthIndex += 1;
                            if (monthIndex > 11) {
                                monthIndex = 0;
                            }
                        }

                        AvailableAccChart.updateOptions({
                            series: [{
                                    data: dynValue
                                },
                                {
                                    data: dynTargetAvailability
                                }
                            ],
                            xaxis: {
                                categories: dynCategories
                            }
                        });

                        /**
                         * Trouble Frequency & MTBF
                         */
                        var tf = grap.troublefreq
                        var dynTargetTroublefreq = [],
                            dynCategoriesTroublefreq = [],
                            dynValueTroublefreq = []

                        var monthIndex = 0;
                        for (var i = 0; i < tf.length; i++) {
                            var datVal = tf[i]
                            dynTargetTroublefreq.push(datVal.trouble)
                            dynCategoriesTroublefreq.push(month[monthIndex] + ' ' + datVal.tahun)
                            dynValueTroublefreq.push(datVal.mtbf)
                            monthIndex += 1;
                            if (monthIndex > 11) {
                                monthIndex = 0;
                            }
                        }

                        mtbfChart.updateOptions({
                            series: [{
                                    data: dynTargetTroublefreq
                                },
                                {
                                    data: dynValueTroublefreq
                                }
                            ],
                            xaxis: {
                                categories: dynCategoriesTroublefreq
                            }
                        });

                        /**
                         * MTTR
                         */
                        var mttr = grap.mttr
                        var dynTargetMttr = [],
                            valTargetMttr = 2.00,
                            dynCategoriesMttr = [],
                            dynValueMttr = []

                        var monthIndex = 0;
                        for (var i = 0; i < mttr.length; i++) {
                            var datVal = mttr[i]
                            dynTargetMttr.push(valTargetMttr)
                            dynCategoriesMttr.push(month[monthIndex] + ' ' + datVal.tahun)
                            dynValueMttr.push(datVal.value)
                            monthIndex += 1;
                            if (monthIndex > 11) {
                                monthIndex = 0;
                            }
                        }

                        mttrChart.updateOptions({
                            series: [{
                                    data: dynValueMttr
                                },
                                {
                                    data: dynTargetMttr
                                }
                            ],
                            xaxis: {
                                categories: dynCategoriesMttr
                            }
                        });

                        /**
                         * Mekanikal
                         */
                        var meka = grap.mekanikal
                        var dynCategoriesMeka = [],
                            dynValueMeka = []

                        for (var i = 0; i < meka.length; i++) {
                            var datVal = meka[i]
                            dynCategoriesMeka.push(datVal.trouble)
                            dynValueMeka.push(parseFloat(datVal.total))
                        }

                        // console.log(dynCategoriesMeka, dynValueMeka)

                        MekanicalChart.updateOptions({
                            series: [{
                                data: dynValueMeka
                            }],
                            xaxis: {
                                categories: dynCategoriesMeka
                            }
                        });

                        /**
                         * Elektrikal
                         */
                        var Elek = grap.elektrikal
                        var dynCategoriesElek = [],
                            dynValueElek = []

                        for (var i = 0; i < Elek.length; i++) {
                            var datVal = Elek[i]
                            dynCategoriesElek.push(datVal.trouble)
                            dynValueElek.push(parseFloat(datVal.total))
                        }

                        // console.log(dynCategoriesElek, dynValueElek)

                        ElektricalChart.updateOptions({
                            series: [{
                                data: dynValueElek
                            }],
                            xaxis: {
                                categories: dynCategoriesElek
                            }
                        });
                    }
                }
            }
        })

    }

    var dateRange = function() {
        flatpickr("#dateRange", {
            mode: 'range',
            altInput: true,
            altFormat: 'd M, Y',
            onChange: function(selectedDates, dateStr, instance) {
                // console.log('change', selectedDates)
            },
            onClose: function(selectedDates, dateStr, instance) {
                var start_date = new Date(selectedDates[0])
                var end_date = new Date(selectedDates[1])
                    // if (start_date.getDate() + start_date.getMonth() + start_date.getFullYear() == end_date.getDate() + end_date.getMonth() + end_date.getFullYear()) {
                    //     console.log(start_date)
                    // } else {
                    //     console.log(selectedDates)
                    // }
                var purgeStart = start_date.getFullYear() + '-' + ((start_date.getMonth() + 1 < 10) ? '0' + (start_date.getMonth() + 1) : (start_date.getMonth() + 1)) + '-' + ((start_date.getDate() < 10) ? '0' + (start_date.getDate()) : start_date.getDate())
                var purgeEnd = end_date.getFullYear() + '-' + ((end_date.getMonth() + 1 < 10) ? '0' + (end_date.getMonth() + 1) : (end_date.getMonth() + 1)) + '-' + ((end_date.getDate() < 10) ? '0' + (end_date.getDate()) : end_date.getDate())
                loadData(purgeStart, purgeEnd)
            }
        })

        $('#tahunFilter').on('change', function() {
            var start, end
            if ($(this).val() == '') {
                start = '', end = ''
            } else {
                start = $(this).val() + '-01-01'
                end = $(this).val() + '-12-31'
            }
            loadData(start, end)
        })
    }

    var initGraphic = function() {
        ExecutionRate();
        DowntimeRatio();
        AvailableAcc();
        MtbfChart()
        MttrChart()
        Mekanical()
        Elektrical()
    }

    var photoGrap = function() {
        if ($('#dashboard1').hasClass('active')) {
            $('#dashboard1').removeClass('active')
            $('#dashboard2').addClass('active').fadeIn()
        } else {
            $('#dashboard2').removeClass('active')
            $('#dashboard1').addClass('active').fadeIn()
        }
    }

    return {
        run: function() {
            initGraphic();
            dateRange()
            var start = $('#tahunFilter').val() + '-01-01'
            var end = $('#tahunFilter').val() + '-12-31'
            loadData(start, end)

            var i = 1
            setInterval(function() {
                var x = i < 10 ? '0' + i : i
                $('#cooldownDashboard').val('00:' + x)
                i += 1

                if (i == 31) {
                    photoGrap()
                    i = 1;
                }
            }, 1000)

            $('#ubahGrafik').on('click', function() {
                i = 0
                photoGrap()
            })

            // setInterval(function () {
            //     if ($('#dashboard1').hasClass('active')) {
            //         $('#dashboard1').removeClass('active')
            //         $('#dashboard2').addClass('active')
            //     } else {
            //         $('#dashboard2').removeClass('active')
            //         $('#dashboard1').addClass('active')
            //     }
            // }, 40000)
        },
        resetDate: function() {
            $('#dateRange').parent('div').find('input').val('')
            loadData()
        }
    }
})();

jQuery(document).ready(function() {
    ExAsTroubleShoot.run()
})