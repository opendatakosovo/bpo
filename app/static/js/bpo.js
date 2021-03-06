var allData = undefined;
var global_division = '';
var global_district = '';
var global_upazila = '';

$(document).ready(function () {

    // Get selected violence type dropdown
    buildViolenceTypeDropDown();

    // Build the date range input so we can select FROM - TO daterange
    buildDateRangeInput();

    // Populate the global allData variable
    allData = getData(true);

    $('.update-chart').change(function () {
        allData = getData(false);
    });


    $('#data-source-select').change(function () {
        buildViolenceTypeDropDown();
        var dataset = $(this).val();

        if (dataset == 'idams') {
            $("#dt1").datepicker('setDate', '01/06/2015');
            $("#dt2").datepicker('setDate', '29/06/2016');
        } else {
            $('#dt1').datepicker('setDate', '01/01/2015');
            $('#dt2').datepicker('setDate', '01/01/2016');
        }
    });

});

function initResizeChartsOnResizeWindow() {
    $(window).resize(function () {
        $("#third-section-first-chart").highcharts().setSize($('#national-accordion').width(), '180', doAnimation = true);
        $("#third-section-second-chart").highcharts().setSize($('#national-accordion').width(), '180', doAnimation = true);
        $("#third-section-third-chart").highcharts().setSize($('#national-accordion').width(), '180', doAnimation = true);
        $("#map").highcharts().setSize($("#map").width(), $("#map").height(), doAnimation = true);
    });
}

function initAccordions() {
    // Initialize the right accordions
    $("#national-accordion").accordion({
        collapsible: true, active: false
    });
    $("#national-rank-accordion").accordion({
        collapsible: true, active: false,
        autoHeight: true
    });
    $("#district-rank-accordion").accordion({
        collapsible: true, active: false,
        autoHeight: true
    });
    $("#division-rank-accordion").accordion({
        collapsible: true, active: false,
        autoHeight: true
    });
}
function buildRankingBasedOnLocation() {

    // National stats accordion
    $('#national-rank-accordion .national-overview-tab').click(function () {
        $('#national-rank-accordion .national-overview-tab').hide();
    });
    $('.collapse-national-stats').click(function () {
        $('#national-rank-accordion .national-overview-tab').click();
        $('#national-rank-accordion .national-overview-tab').show();
    });

    // Division stats accordion
    $('#division-rank-accordion .division-overview-tab').click(function () {
        $('#division-rank-accordion .division-overview-tab').hide();
    });
    $('.collapse-division-stats').click(function () {
        $('#division-rank-accordion .division-overview-tab').click();
        $('#division-rank-accordion .division-overview-tab').show();
    });

    // District stats accordion
    $('#district-rank-accordion .district-overview-tab').click(function () {
        $('#district-rank-accordion .district-overview-tab').hide();
    });
    $('.collapse-district-stats').click(function () {
        $('#district-rank-accordion .district-overview-tab').click();
        $('#district-rank-accordion .district-overview-tab').show();
    });
}

function populateLocationDropdown() {
    // Listen when we change the division/Update the visualizer reflecting the selected division data
    var availableTags = [];

    $.each(grouped_locations_list, function (i, item) {
        availableTags.push(item.division);
        availableTags.push(item.division + ', ' + item.district);
    });
    var uniqueNames = [];
    $.each(availableTags, function (i, el) {
        if ($.inArray(el, uniqueNames) === -1) uniqueNames.push(el);
    });
    $("#division-select").autocomplete({
        source: uniqueNames,
        select: function (event, ui) {
            selected_vals = ui.item.label.split(',');
            doDrillDown(selected_vals);
            allData = getData(false);

        }
    });

}
function doDrillDown(dDownArray) {
    global_division = "";
    global_upazila = "";
    global_district = "";
    $('.highcharts-drillup-button').click();
    $('.highcharts-drillup-button').click();
    $.each(dDownArray, function (item) {
        if (item < 2) {
            var map_data_ = $('#map').highcharts().series[0].data;
            $.each(map_data_, function (index) {
                if (map_data_[index]['name'] == dDownArray[item].trim()) {
                    map_data_[index].doDrilldown();
                }
            });
        }

    });

}
function initCharts() {

    var categories = [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec'
    ]

    var deaths_data_series = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    var injuries_data_series = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    var property_damage_data_series = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    var width = $("#third-section-first-chart").width();
    var chart_options = {
        renderTo: 'chart',
        type: 'column',
        margin: 70,
        height: 180,
        defaultSeriesType: 'areaspline'
    }

    var chart1 = Highcharts.chart('third-section-first-chart', {
        chart: {
            renderTo: 'third-section-first-chart',
            type: 'column',
            margin: 70,
            height: 180,
            defaultSeriesType: 'areaspline',
            description: "Time  chart based on number of deaths count."
        },
        title: {
            text: ''
        },
        xAxis: {
            tickPixelInterval: 50,
            categories: categories,
            crosshair: true
        },
        yAxis: {
            gridLineWidth: 0,
            minorGridLineWidth: 0,
            min: 0,
            position: 'right',
            title: {
                text: 'Nr. of deaths'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="padding:0"><b>{point.y}</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            series: {
                stacking: 'normal',
                borderWidth: 0
            },
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        navigator: {
            series: {
                includeInCSVExport: false
            }
        },
        series: [{
            name: "Deaths",
            data: deaths_data_series

        }],
        exporting: {
            csv: {
                dateFormat: '%Y-%m-%d'
            }
        }
    });
    var chart2 = Highcharts.chart('third-section-second-chart', {
        chart: {
            renderTo: 'third-section-second-chart',
            type: 'column',
            margin: 70,
            height: 180,
            defaultSeriesType: 'areaspline',
            description: "Time chart based on number of injury count."
        },
        title: {
            text: ''
        },
        xAxis: {
            categories: categories,
            crosshair: true
        },
        yAxis: {
            min: 0,
            position: 'right',
            title: {
                text: 'Nr. of injuries'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="padding:0"><b>{point.y}</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        navigator: {
            series: {
                includeInCSVExport: false
            }
        },
        series: [{
            name: 'Injuries',
            data: injuries_data_series

        }],
        exporting: {
            csv: {
                dateFormat: '%Y-%m-%d'
            }
        }
    });
    var chart3 = Highcharts.chart('third-section-third-chart', {
        chart: {
            renderTo: 'third-section-third-chart',
            type: 'column',
            margin: 70,
            height: 180,
            defaultSeriesType: 'areaspline',
            description: "Time chart based on number of property damage count."
        },
        title: {
            text: ''
        },
        xAxis: {
            categories: categories,
            crosshair: true
        },
        yAxis: {
            min: 0,
            position: 'right',
            title: {
                text: 'Nr. of property damage'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="padding:0"><b>{point.y}</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        navigator: {
            series: {
                includeInCSVExport: false
            }
        },
        series: [{
            name: 'Property damage',
            data: property_damage_data_series

        }],
        exporting: {
            csv: {
                dateFormat: '%Y-%m-%d'
            }
        }
    });


}
function getName() {
    if (global_division != "" && global_district == "" && global_upazila == "") {
        return global_division + " Division";
    }
    if (global_division != "" && global_district != "" && global_upazila == "") {
        return global_division + " Division, " + global_district + " District";
    }
    if (global_division != "" && global_district != "" && global_upazila != "") {
        return global_division + ", " + global_district + ", " + global_upazila + "";
    }
    if (global_division == "" && global_district == "" && global_upazila == "") {
        return "Bangladesh";
    }
}
function download(filename, text) {
    var pom = document.createElement('a');
    pom.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(text));
    pom.setAttribute('download', filename);

    if (document.createEvent) {
        var event = document.createEvent('MouseEvents');
        event.initEvent('click', true, true);
        pom.dispatchEvent(event);
    }
    else {
        pom.click();
    }
}
function buildNationalData() {
    // Set the highest rates
    var top_death_location = getTopN(allData['rank-stats'], 'death', 1)[0].name;
    var top_injury_location = getTopN(allData['rank-stats'], 'injury', 1)[0].name;
    var top_property_damage_location = getTopN(allData['rank-stats'], 'property', 1)[0].name;
    $('.rate-1').html(top_death_location);
    $('.rate-2').html(top_injury_location);
    $('.rate-3').html(top_property_damage_location);

    updateCharts();
    updateTop3Section();
    updateRankSections();
    updateCensusInfo();
}
function getDate() {
    // Get date
    var date_1 = $('#dt1').val().split('/');
    date_1 = date_1[1] + '-' + date_1[0] + '-' + date_1[2];
    var date_2 = $('#dt2').val().split('/');
    date_2 = date_2[1] + '-' + date_2[0] + '-' + date_2[2];
    var date = (date_1 + '---' + date_2);
    return date;
}
function getData(init) {

    var dataResults = undefined;
    var division = "";
    var district = "";
    var upazila = "";


    // Get the selected dataset
    var dataset = $('#data-source-select').val();

    // Get selected violence type dropdown
    var violence_type = $("#violence-type-select").val().replace('/', '-');

    // Get selected daterange
    var date = getDate();

    if (init == false) {
        if ($('#map').highcharts().drilldownLevels != undefined) {
            if ($('#map').highcharts().drilldownLevels.length == 2) {
                district = $('#map').highcharts().drilldownLevels[1].lowerSeriesOptions.name;
                global_district = district;
                division = $('#map').highcharts().drilldownLevels[0].lowerSeriesOptions.name;
                global_division = division;
            } else if ($('#map').highcharts().drilldownLevels.length == 1) {
                division = $('#map').highcharts().drilldownLevels[0].lowerSeriesOptions.name
                global_division = division;
            }
        }
    }

    var jsonData = {
        "division": global_division,
        "district": global_district,
        "upazila": global_upazila,
        "date": date,
        "violence_type": violence_type,
        "dataset": dataset,
        "period": "monthly"
    };

    $.ajax('/api/search', {
        type: "POST",
        contentType: 'application/json',
        data: JSON.stringify(jsonData),
        beforeSend: function () {
            $('#loadingmessage').show();
        },
        success: function (data) {
            allData = data;
            if (init == true) {
                init_viz();
            } else {
                updateViz();
                $('#loadingmessage').hide();
            }
            if (division == "") {
                $('.location-name').html(" Bangladesh");
            } else if (global_division != "" && global_district == "") {
                $('.location-name').html(global_division + ' Division');
            } else if (division != "" && global_district != "") {
                $('.location-name').html(global_division + " Division, " + global_district + ' District');
            } else if (global_division != "" && global_district != "" && global_upazila != "") {
                $('.location-name').html(global_division + " Division, " + global_district + ' District, ' + global_upazila + ' Upazila');
            }
            return data;
        }
    });

}
function init_viz() {
    // Init and build the map
    buildMap();
    // Init the right death,injuries,property charts
    initCharts();

    // Init and build the national data, so when the user first lands on the page we have some data.
    buildNationalData();

    // Init and create the bottom line chart
    createLineChart();

    // Init the jQuery UI accordions
    initAccordions();

    // Resize charts on window resize
    initResizeChartsOnResizeWindow();

    // Build the ranking on the right on location based stats
    buildRankingBasedOnLocation();

    // Populate location searchbox dropdown list
    populateLocationDropdown();

    // Init and build the violence type dropdown list
//        $('#violence-type-select [value="Attack: Coordinated action each-other political parties, groups, fractions and authorities"]').attr('selected', true);
    $('#loadingmessage').hide();
}
function updateRankSections() {
    var rank_data = allData['stats'];
    var match_name = "";
    if (global_division != '' && global_district == "") {
        match_name = global_division;
        $('#division-rank').show();
    } else if (global_division != '' && global_district != "") {
        match_name = global_district;
        $('#division-rank').show();
    } else {
        $('#division-rank').hide();
    }

    // Set death ranks
    if (rank_data['death'] != undefined) {
        $.each(rank_data['death'], function (i, item) {
            if (item.name == match_name) {
                $('.division-death-rank-nth').text(item['rank'] + 'th');
                $('.division-desc-death-rank-name').text(item['name']);
                $('.division-desc-death-rank').text(item['rank']);
                $('.division-desc-death-rank-total').text(Math.round(item['total']));
            }
        });
    }

    // Set injury ranks
    if (rank_data['injury'] != undefined) {
        $.each(rank_data['injury'], function (i, item) {
            if (item.name == match_name) {
                $('.division-injury-rank-nth').text(item['rank'] + 'th');
                $('.division-desc-injury-rank-name').text(item['name']);
                $('.division-desc-injury-rank').text(item['rank']);
                $('.division-desc-injury-rank-total').text(Math.round(item['total']));
            }
        });
    }
    // Set Property Damage ranks
    if (rank_data['property'] != undefined) {
        $.each(rank_data['property'], function (i, item) {
            if (item.name == match_name) {
                $('.division-property-rank-nth').text(item['rank'] + 'th');
                $('.division-desc-property-rank-name').text(item['name']);
                $('.division-desc-property-rank').text(item['rank']);
                $('.division-desc-property-rank-total').text(Math.round(item['total']));
            }
        });
    }

}
function createLineChart() {
    function titleMove(e) {
        var title = this.legend.title;
        if ($(window).width() > 768) {
            if (title != undefined) {
                title.translate(-80, 28);
            }
        }

    }

    var seriesOptions = [];
    var seriesCounter = 0;
    var names = ['Deaths', 'Injuries', 'Incidents', 'Property Damage'];

    /**
     * Create the chart when all data is loaded
     * @returns {undefined}
     */
    var isBig = $(window).width() > 768;

    var legendBig = {
        enabled: true,
        align: 'right',
        backgroundColor: '#fff',
        layout: 'horizontal',
        verticalAlign: 'right',
        symbolWidth: 0,
        y: -25,
        useHTML: true,
        labelFormatter: function () {
            return '<div class="line-chart-item" style="height: 22px;background-color:' + this.color + '; border: 1px solid rgba(0,0,0,0.08);border-radius: 22px;padding-left:10px;padding-right:10px;"> <input class="line-chart-checkbox ' + this.name + '" type="checkbox" > <span style="font-family: Roboto;font-size: 11px;line-height: 13px;color: #FFFFFF;">' + this.name + '</span></div>';
        },
        title: {
            text: "Filter data:",
            style: "margin-left:-30px;"
        },
    };

    var legendSmall = {
        enabled: true,
        align: 'right',
        layout: 'vertical',
        verticalAlign: 'right',
        horizontalAlign: "right",
        symbolWidth: 0,
        x: -20,
        y: 20,
        useHTML: true,
        labelFormatter: function () {
            return '<div class="line-chart-item" style="width:138px; height: 22px;background-color:' + this.color + '; border: 1px solid rgba(0,0,0,0.08);border-radius: 22px;padding-left:10px;padding-right:10px;"> <input class="line-chart-checkbox ' + this.name + '" type="checkbox" style="border-radius: 6px; " > ' + this.name + ' </div>';
        }
    };


    function createChart(seriesOptions) {
        var date_start = $('#dt1').val().split('/');
        var start_point = Date.UTC(date_start[2], date_start[0], date_start[1]);
        var chart = Highcharts.stockChart({
            exporting: {
                csv: {
                    dateFormat: '%Y-%m-%d'
                }
            },
            chart: {
                type: 'line',
                events: {
                    load: titleMove,
                    redraw: titleMove
                },
                renderTo: 'line-chart-container',
                height: 400,
                description: "Time based linechart.",
                zoomType: 'x'
            },
            rangeSelector: {
                inputEnabled: false,
                selected: 5
            },

            yAxis: {
                labels: {
                    formatter: function () {
                        return this.value;
                    }
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: 'silver',

                }],
                min: 0
            },
            xAxis: {
                type: 'datetime',
            },
            plotOptions: {

                series: {
                    compare: 'value',
                    showInNavigator: true,
                    stacking: false,
                    pointStart: start_point,
                    pointInterval: 24 * 3600 * 1000 // one day
                },
                dataGrouping: {
                    forced: true,
                    units: [
                        ['days', [1]]
                    ]
                }
            },

            tooltip: {
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>',
                valueDecimals: 0,
                split: true
            },
            legend: isBig ? legendBig : legendSmall,
            navigator: {
                series: {
                    includeInCSVExport: false
                }
            },
            series: seriesOptions,


        });
        $('.line-chart-checkbox.Incidents').click();
        // $('#Human_and_Economic_Impact_Download').click(function () {
        //     download('Human_and_Economic_Impact.csv', chart.getCSV());
        // });

    }

    $.each(names, function (i, name) {
        var deaths = [];
        var injuries = [];
        var incidents = [];
        var property_damage = [];
        var data = allData['daily-stats'];
        $.each(data, function (item) {
            if (data[item]['date'] != null) {
                incidents.push([data[item]['date'].$date, data[item]['incidents']])
                deaths.push([data[item]['date'].$date, data[item]['death']])
                injuries.push([data[item]['date'].$date, data[item]['injuries']])
                property_damage.push([data[item]['date'].$date, data[item]['property']])

            }
        })

        if (name == 'Deaths') {
            seriesOptions[i] = {
                name: name,
                color: '#ED7D31',
                data: deaths,
                selected: false,
                visible: false
            };
        }
        if (name == 'Injuries') {
            seriesOptions[i] = {
                name: name,
                color: "#A5A5A5",
                data: injuries,
                selected: false,
                visible: false
            };
        }

        if (name == 'Incidents') {
            seriesOptions[i] = {
                name: name,
                color: "#FFC000",
                data: incidents,
                selected: true,
                visible: false
            };
        }


        // As we're loading the data asynchronously, we don't know what order it will arrive. So
        // we keep a counter and create the chart when all the data is loaded.
        seriesCounter += 1;

        if (seriesCounter === names.length) {
            createChart(seriesOptions);
        }
    });
    $('.line-chart-item').click(function () {
        if ($(this).children().is(':checked') == true) {
            $(this).children().removeAttr("checked");
        } else {
            $(this).children().prop('checked', true);
        }

        $.each(Highcharts.charts, function (item) {
            if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'line-chart-container') {
                $.each(Highcharts.charts[item].series, function (index) {
                    var axisMax = Highcharts.charts[item].yAxis[0].max; // Max of the axis
                    var dataMax = Highcharts.charts[item].yAxis[0].dataMax; // Max of the data
                    var xaxisMax = Highcharts.charts[item].xAxis[0].max;
                });
                Highcharts.charts[item].redraw();
            }
        });
    });
    $('.line-chart-checkbox').click(function () {
        if ($(this).is(':checked') == true) {
            $(this).removeAttr("checked");
        } else {
            $(this).prop('checked', true);
        }
    })


}

function updateLineChart() {
    var deaths = [];
    var injuries = [];
    var incidents = [];
    var property_damage = [];
    var data = allData['daily-stats'];
    $.each(data, function (item) {
        if (data[item]['date'] != null) {
            deaths.push([data[item]['date'].$date, data[item]['death']])
            injuries.push([data[item]['date'].$date, data[item]['injuries']])
            property_damage.push([data[item]['date'].$date, data[item]['property']])
            incidents.push([data[item]['date'].$date, data[item]['incidents']])
        }
    })
    $.each(Highcharts.charts, function (item) {
        if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'line-chart-container') {
            $.each(Highcharts.charts[item].series, function (index) {
                var name = Highcharts.charts[item].series[index].name;
                if (name == 'Deaths') {
                    Highcharts.charts[item].series[index].setData(deaths);
                } else if ('Injuries') {
                    Highcharts.charts[item].series[index].setData(injuries);
                } else if ('Incidents') {
                    Highcharts.charts[item].series[index].setData(incidents);
                } else if ('Property Damage') {
                    Highcharts.charts[item].series[index].setData(property_damage);
                }
            });
            Highcharts.charts[item].redraw();
        }
    });
}
function buildDateRangeInput() {
    // Add daterange jquery functionality
    var startDate, endDate, dateRange = [];
    $("#dt1").datepicker({
        dateFormat: 'dd/mm/yy'
    });
    $("#dt2").datepicker({
        dateFormat: 'dd/mm/yy'
    });

    $("#dt1").datepicker('setDate', "01/06/2014");
    $("#dt2").datepicker('setDate', "29/06/2015");

}
function buildMap() {
    var map_data = buildDataSeries();
    /*
     TODO:
     - Check data labels after drilling. Label rank? New positions?
     - Not US Mainland text
     - Separators
     */
    var mapData = Highcharts.maps['countries/bd/bd-all'];
    var myData = Highcharts.geojson(Highcharts.maps['countries/bd/bd-all']);
    var tempSeries;

    // Some responsiveness
    var small = $('#map').width() < 500;

    // Set drilldown pointers
    $.each(myData, function (i) {
        this['hc-key'] = this.properties['hc-key'];
        this.drilldown = this.properties['name'];
        if (map_data['division'][this.name] != undefined) {
            this.value = map_data['division'][this.name];
        } else {
            this.value = null;
        }
        this.location_type = 'division';
        this.level = 1;
    });

    // Instanciate the map
    $('#map').highcharts('Map', {
        chart: {
            renderTo: 'map',
            height: 550,
            description: "Incident distribution map.",
            events: {
                drilldown: function (e) {
                    map_data = buildDataSeries();
                    var map_key;
                    var drilldown_level = e.point.level;
                    if (drilldown_level == 1) {
                        map_key = 'countries/bd/bd-districts-all';
                    } else if (drilldown_level == 2) {
                        map_key = 'countries/bd/bd-upazillas-all';
                    }
                    var chart = this;
                    var name = e.point.name;
                    // Font Awesome spinner

                    // Load the drilldown map
                    var data = Highcharts.maps[map_key];
                    var drillMyData = Highcharts.geojson(data);
                    var drilldown_data = [];

                    // Set a non-random bogus value

                    $.each(drillMyData, function (i) {
                        if (drilldown_level == 1) {
                            if (this.properties['Division'] == name) {
                                this['hc-key'] = "bd-" + this.properties['District'].substr(0, 2).toLowerCase();
                                this.name = this.properties['District'];
                                if (map_data['district'][this.name] != undefined) {
                                    this.value = map_data['district'][this.name];
                                } else {
                                    this.value = null;
                                }
                                this.drilldown = this.properties.District;
                                this.level = 2;
                                drilldown_data.push(this);
                            }
                        } else if (drilldown_level == 2) {
                            if (this.properties.District == name) {
                                this['hc-key'] = "bd-" + this.properties['Upazila'].substr(0, 2).toLowerCase();
                                this.name = this.properties['Upazila'];
                                if (map_data['upazila'][this.name] != undefined) {
                                    this.value = map_data['upazila'][this.name];
                                } else {
                                    this.value = null;
                                }
                                this.level = 3;
                                drilldown_data.push(this);
                            }
                        }
                    });

                    chart.addSeriesAsDrilldown(e.point, {
                        name: e.point.name,
                        data: drilldown_data.slice(0, drillMyData.length),
                        joinBy: 'hc-key',
                        dataLabels: {
                            enabled: true,
                            format: '{point.name}'
                        }
                    });
                    // Hide loading and add series
                    chart.hideLoading();


                    this.setTitle(null, {text: e.point.name});
                },
                drillup: function (e) {
                    global_division = "";
                    global_district = "";
                    global_upazila = "";
                    allData = getData(false);
                }
            }
        },

        title: {
            text: ' '
        },

        subtitle: {
            text: '',
            floating: true,
            align: 'right',
            y: 50,
            style: {
                fontSize: '16px'
            }
        },

        legend: small ? {} : {
            title: {
                text: "No of Incidents"
            },
            itemStyle: {
                'font-family': "Noto Serif",
                'font-size': '14px !important',
                'font-weight': 'bold',
                'line-height': '19px',
                'color': '#333333'
            },
            layout: 'vertical',
            borderWidth: 1,
            symbolRadius: 0,
            boxShadow: '-1px 2px 2px 0 rgba(0, 0, 0, 0.2)',
            align: 'right',
            verticalAlign: 'top',
            y: -5,
            labelFormatter: function () {
                if (this.from === undefined) {
                    return '< ' + this.to;
                }

                if (this.to === undefined) {
                    return '> ' + this.from;
                }

                return this.from + ' to ' + this.to;
            }
        },
        credits: {
            text: '* Click area(drill down) to see results.<br/>',
            position: {
                align: 'center',
                y: -5 // position of credits
            },
            style: {
                fontSize: '11pt' // you can style it!
            }
        },
        colorAxis: {
            dataClasses: [{
                from: 0,
                to: 10,
                color: "#a3dbb9"
            }, {
                from: 11,
                to: 20,
                color: "#fbfa20"
            }, {
                from: 21,
                to: 40,
                color: "#f8c733"
            }, {
                from: 41,
                to: 60,
                color: "#feb126"
            }, {
                from: 61,
                to: 100,
                color: "#f7802d"
            }, {
                from: 101,
                to: 150,
                color: "#c56624"
            }, {
                from: 151,
                to: 200,
                color: "#c56626"
            }, {
                from: 201,
                to: 300,
                color: "#ac591f"
            }, {
                from: 301,
                to: 500,
                color: "#944c1b"
            }, {
                from: 501,
                color: "#7b4016"
            }]
        },

        mapNavigation: {
            enableMouseWheelZoom: false,
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },

        plotOptions: {
            map: {
                states: {
                    hover: {
                        color: '#a1a1a1'
                    }
                }
            },
            series: {
                point: {
                    events: {
                        click: function (i) {
                            if (i.target.className.baseVal.split(' ')[1] != undefined) {
                                var clicked_point = capitalize(i.target.className.baseVal.split(' ')[1].split('-')[2]);
                                if ($(i.target)[0].point != null && global_upazila == "") {
                                    global_upazila = $(i.target)[0].point.options.properties.Upazila;
                                } else {
                                    global_upazila = "";
                                }
                                allData = getData(false);
                                return clicked_point;
                            } else {
                                var clicked_point = $(i.target)[0].textContent;
                                allData = getData(false);
                                return clicked_point;
                            }
                        }
                    }
                }
            }
        },

        series: [{
            data: myData,
            mapData: mapData,
            joinBy: 'name',
            name: 'Bangladesh',
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            },

        }],

        drilldown: {
            //series: drilldownSeries,
            activeDataLabelStyle: {
                color: '#FFFFFF',
                textDecoration: 'none',
                textShadow: '0 0 3px #000000'
            },
            drillUpButton: {
                relativeTo: 'spacingBox',
                position: 'left',
                theme: {
                    fill: '#FFA400',
                    'stroke-width': 1,
                    stroke: 'white',
                    r: 14,
                    states: {
                        hover: {
                            fill: '#1B6D85'
                        },
                        select: {
                            stroke: '#039',
                            fill: '#a4edba'
                        }
                    }
                }
            }
        }
    });

}
function updateViz() {
    // If we are in the country version we should build national data visualizer

    updateTextValues();
    updateCharts();
    updateMapValues();
    updateLineChart();
    updateRankSections();
    updateTop3Section();
    updateCensusInfo();
    $('#map').highcharts().redraw();
}
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
function updateCensusInfo() {
    var data = allData['census'][0]
    if (data != null) {
        $('.population-data').text(numberWithCommas(data['population']));
        if (data['poverty'] != null) {
            $('.poverty-data').css('display', '');
            $('.poverty-data').text(data['poverty'] + "%");
        } else {
            $('.poverty-data').css('display', 'none');
            $('.poverty-data').text(data['poverty'] + "%");
        }
        var total = data['muslim'] + data['hindu'] + data['christian'] + data['buddhist'] + data['other'];
        var percentage_of_muslims = String(data['muslim'] * 100 / total).substring(0, 4);
        var percentage_of_hindu = String(data['hindu'] * 100 / total).substring(0, 4);
        var percentage_of_christian = String(data['christian'] * 100 / total).substring(0, 4);
        var percentage_of_buddhist = String(data['buddhist'] * 100 / total).substring(0, 4);
        var percentage_of_other = String(data['other'] * 100 / total).substring(0, 4);

        $('#muslim-data').text(percentage_of_muslims);
        $('#hindu-data').text(percentage_of_hindu);
        $('#christian-data').text(percentage_of_christian);
        $('#buddhist-data').text(percentage_of_buddhist);
        $('#others-data').text(percentage_of_other);
    }
}
// Update the text trend values reflecting the selections
function updateTextValues() {
    //Instantiate rank_data array
    var rank_data = allData['rank-stats'];

    // Get top death location name
    death_top_rank_data = getTopN(rank_data, 'death', 1);
    var top_death_location = "";
    if (death_top_rank_data.length != 0) {
        $('.rate-1-text').html('has the highest fatality rate.')
        $('.rate-1').parent().removeClass("ui-state-disabled");
        top_death_location = death_top_rank_data[0].name;
        $('.rate-1').html(top_death_location);
    } else {
        $('.rate-1').html("");
        $('.rate-1-text').html('Not enough data');
        $('.rate-1').parent().addClass("ui-state-disabled");
    }

    // Get top injury location name
    injury_top_rank_data = getTopN(rank_data, 'injury', 1)
    var top_injury_location = "";
    if (injury_top_rank_data.length != 0) {
        $('.rate-2-text').html('has the highest injury count.');
        $('.rate-2').parent().removeClass("ui-state-disabled");
        top_injury_location = injury_top_rank_data[0].name;
        $('.rate-2').html(top_injury_location);
    } else {
        $('.rate-2').html("");
        $('.rate-2-text').html('Not enough data');
        $('.rate-2').parent().addClass("ui-state-disabled");
    }

    // Get top property damage location name
    property_top_rank_data = getTopN(rank_data, 'property', 1);
    var top_property_damage_location = "";
    if (property_top_rank_data.length != 0) {
        $('.rate-3-text').html('has the highest property damage count.');
        $('.rate-3').parent().removeClass("ui-state-disabled");
        top_property_damage_location = property_top_rank_data[0].name;
        $('.rate-3').html(top_property_damage_location);
    } else {
        $('.rate-3').html("");
        $('.rate-3').parent().addClass("ui-state-disabled");
        $('.rate-3-text').html('Not enough data');
    }


    // Change the presentation text based on the level
    if (global_division == "" && global_district == "" && global_upazila == "") {
        $('.section-title').text('National Overview of Divisions:');
    }
    else if (global_division != "" && global_district == "" && global_upazila == "") {
        $('.section-title').text('Division Overview:');
        $('.rank-section-title').text('National Rank of ' + global_division + ' Division:');
    }
    else if (global_division != "" && global_district != "" && global_upazila == "") {
        $('.section-title').text('District Overview:');
        $('.rank-section-title').text('National Rank of ' + global_district + ' District:');
    }
}

// Update charts in the accordions reflecting the selections
function updateCharts() {
    // Get date
    var date = getDate();
    var new_date = date.split('---');
    var timeDiff = Math.abs((new Date(new_date[0])).getTime() - (new Date(new_date[1])).getTime())
    var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
    if (diffDays <= 365) {
        var data = allData['monthly-stats'];
        var data_series_array = Array.apply(null, Array(12)).map(Number.prototype.valueOf, 0);
        var categories = [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec'
        ]
        $.each(Highcharts.charts, function (item) {
            if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'third-section-first-chart') {

                // Update third-section-first-chart values
                $.each(data, function (item) {
                    if (data[item].death != 0) {
                        data_series_array[parseInt(data[item].month) - 1] = data[item].death;
                    }
                });

                // Populate data series array and show the message if there is no data
                if (data_series_array.reduce(add, 0) != 0) {
                    $('.rate-1').parent().removeClass("ui-state-disabled");
                    Highcharts.charts[item].series[0].setData(data_series_array);
                    Highcharts.charts[item].xAxis[0].setCategories(categories);
                    updateTrendArrows(data_series_array, 1);
                    Highcharts.charts[item].hideLoading();
                } else {
                    $('.rate-1').parent().addClass("ui-state-disabled");
                    data_series_array = Array.apply(null, Array(12)).map(Number.prototype.valueOf, 0);
                    Highcharts.charts[item].series[0].setData(data_series_array);
                    Highcharts.charts[item].showLoading('No data to display');
                }

                // Reset data series array
                data_series_array = Array.apply(null, Array(12)).map(Number.prototype.valueOf, 0);
            }
            if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'third-section-second-chart') {

                // Update third-section-second-chart values
                $.each(data, function (item) {
                    data_series_array[parseInt(data[item].month) - 1] = data[item].injuries;
                });

                // Populate data series array and show the message if there is no data
                if (data_series_array.reduce(add, 0) != 0) {
                    $('.rate-2').parent().removeClass("ui-state-disabled");
                    Highcharts.charts[item].series[0].setData(data_series_array);
                    Highcharts.charts[item].xAxis[0].setCategories(categories);
                    updateTrendArrows(data_series_array, 2);
                    Highcharts.charts[item].hideLoading();
                } else {
                    $('.rate-2').parent().addClass("ui-state-disabled");
                    // Reset data series array
                    data_series_array = Array.apply(null, Array(12)).map(Number.prototype.valueOf, 0);
                    Highcharts.charts[item].series[0].setData(data_series_array);
                    Highcharts.charts[item].showLoading('No data to display');
                }

                // Reset data series array
                data_series_array = Array.apply(null, Array(12)).map(Number.prototype.valueOf, 0);
            }
            if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'third-section-third-chart') {
                // Update third-section-third-chart values
                $.each(data, function (item) {
                    data_series_array[parseInt(data[item].month) - 1] = data[item].property;
                });

                // Populate data series array and show the message if there is no data
                if (data_series_array.reduce(add, 0) != 0) {
                    $('.rate-3').parent().removeClass("ui-state-disabled");
                    Highcharts.charts[item].series[0].setData(data_series_array);
                    Highcharts.charts[item].xAxis[0].setCategories(categories);
                    updateTrendArrows(data_series_array, 3);
                    $('.rate-3-text .not-enough-data-for-chart-rate-3').remove();
                    Highcharts.charts[item].hideLoading();
                } else {
                    $('.rate-3').parent().addClass("ui-state-disabled");
                    data_series_array = Array.apply(null, Array(12)).map(Number.prototype.valueOf, 0);
                    Highcharts.charts[item].series[0].setData(data_series_array);
                    Highcharts.charts[item].showLoading('No data to display');
                }

                // Reset data series array
                data_series_array = Array.apply(null, Array(12)).map(Number.prototype.valueOf, 0);
            }

        })
    } else {
        var data = allData['quarterly-stats'];
        var third_section_third_chart = $('#third-section-third-chart').highcharts();
        var years = [];
        var data_series_array_chart = [];

        // Build the data series and categories for the charts
        $.each(data, function (item) {
            years.push(data[item].year);
        });
        years = Array.from(new Set(years));

        $.each(years, function (item) {
            data_series_array_chart.push.apply(data_series_array_chart, [0, 0, 0, 0]);
        });

        data_series_array_categories = [];
        $.each(years, function (item) {
            $.each([1, 2, 3, 4], function (index) {
                data_series_array_categories.push("Q" + (index + 1) + " " + years[item].toString().slice(-2));
                ;
            });
        });

        $.each(Highcharts.charts, function (item) {

            if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'third-section-first-chart') {
                // Populate data series array
                $.each(data, function (itemIndex) {
                    var data_index = years.indexOf(data[itemIndex].year) * 4 + (data[itemIndex].quarter - 1);
                    data_series_array_chart[data_index] = data[itemIndex].death;
                });

                // Let's check if we have data and remove the red warning messages
                if (data_series_array_chart.reduce(add, 0) != 0) {
                    $('.rate-1').parent().removeClass("ui-state-disabled");
                    Highcharts.charts[item].series[0].setData(data_series_array_chart);
                    Highcharts.charts[item].xAxis[0].setCategories(data_series_array_categories);
                    $('.not-enough-data-for-chart-rate-1').css('display', 'none');
                    updateTrendArrows(data_series_array_chart, 1);
                    Highcharts.charts[item].hideLoading();
                }
                else {
                    $('.rate-1').parent().addClass("ui-state-disabled");
                    // Reset data series array
                    data_series_array_chart = [];
                    $.each(years, function (item) {
                        data_series_array_chart.push.apply(data_series_array_chart, [0, 0, 0, 0]);
                    });
                    Highcharts.charts[item].series[0].setData(data_series_array_chart);
                    Highcharts.charts[item].showLoading('No data to display');
                }

                // Reset data series array
                data_series_array_chart = [];
                $.each(years, function (item) {
                    data_series_array_chart.push.apply(data_series_array_chart, [0, 0, 0, 0]);
                });
            }
            if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'third-section-second-chart') {

                // Populate data series array
                $.each(data, function (itemIndex) {
                    var data_index = years.indexOf(data[itemIndex].year) * 4 + (data[itemIndex].quarter - 1);
                    data_series_array_chart[data_index] = data[itemIndex].injuries;

                });

                // Let's check if we have data and remove the red warning messages
                if (data_series_array_chart.reduce(add, 0) != 0) {
                    $('.rate-2').parent().removeClass("ui-state-disabled");
                    Highcharts.charts[item].series[0].setData(data_series_array_chart);
                    Highcharts.charts[item].xAxis[0].setCategories(data_series_array_categories);
                    updateTrendArrows(data_series_array_chart, 2);
                    Highcharts.charts[item].hideLoading();
                }
                else {
                    $('.rate-2').parent().addClass("ui-state-disabled");
                    data_series_array_chart = [];
                    $.each(years, function (item) {
                        data_series_array_chart.push.apply(data_series_array_chart, [0, 0, 0, 0]);
                    });
                    Highcharts.charts[item].series[0].setData(data_series_array_chart);
                    Highcharts.charts[item].showLoading('No data to display');
                }

                // Reset data series array
                data_series_array_chart = [];
                $.each(years, function (item) {
                    data_series_array_chart.push.apply(data_series_array_chart, [0, 0, 0, 0]);
                });

            }
            if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'third-section-third-chart') {
                // Populate data series array
                $.each(data, function (itemIndex) {
                    var data_index = years.indexOf(data[itemIndex].year) * 4 + (data[itemIndex].quarter - 1);
                    data_series_array_chart[data_index] = data[itemIndex].property;

                });

                // Let's check if we have data and remove the red warning messages
                if (data_series_array_chart.reduce(add, 0) != 0) {
                    $('.rate-3').parent().parent().removeClass("ui-state-disabled");
                    Highcharts.charts[item].series[0].setData(data_series_array_chart);
                    updateTrendArrows(data_series_array_chart, 3);
                    Highcharts.charts[item].xAxis[0].setCategories(data_series_array_categories);
                    Highcharts.charts[item].hideLoading();
                }
                else {
                    $('.rate-3').parent().addClass("ui-state-disabled");
                    data_series_array_chart = [];
                    $.each(years, function (item) {
                        data_series_array_chart.push.apply(data_series_array_chart, [0, 0, 0, 0]);
                    });
                    Highcharts.charts[item].series[0].setData(data_series_array_chart);
                    Highcharts.charts[item].showLoading('No data to display');
                }
                // Reset data series array
                data_series_array_chart = [];
                $.each(years, function (item) {
                    data_series_array_chart.push.apply(data_series_array_chart, [0, 0, 0, 0]);
                });
            }

        });
    }


}

// Update trend arrays
function updateTrendArrows(array, chartNumber) {
    if (array[array.length - 1] > array[array.length - 2]) {
        $('.rate-' + chartNumber + '-arrow').css('display', '');
        $('.rate-' + chartNumber + '-arrow')[0].src = $('.rate-2-arrow')[0].src.replace('down', 'up');
    } else if (array[array.length - 1] < array[array.length - 2]) {
        $('.rate-' + chartNumber + '-arrow')[0].src = $('.rate-2-arrow')[0].src.replace('up', 'down');
    }
    else if (array[array.length - 1] == array[array.length - 2]) {
        $('.rate-' + chartNumber + '-arrow').css('display', 'none');
    }
}

// Update the top 3 types
function updateTop3Section() {
    // Update the Top 3 values

    var data = allData['top-3'];
    if (data.perpetrator.length != 0) {
        var perpetrators = [];
        $('#perpetrators-list').css('display', '');
        $('.perpetrators-list-not-enogh-data').css('display', 'none');
        $.each(data.perpetrator, function (i, item) {
            perpetrators.push('<li>' + item['perpetrator'] + '</li>');

        });  // close each()

        // Clear list and populate
        $('#perpetrators-list li').remove();
        $('#perpetrators-list').append(perpetrators.join(''));
    } else {
        $('#perpetrators-list').css('display', 'none');
        $('.perpetrators-list-not-enogh-data').css('display', 'block');
    }

    if (data.casualties.length != 0) {
        $('#casualties-list').css('display', '');
        $('.casualties-list-not-enogh-data').css('display', 'none');
        var casualties = [];
        $.each(data.casualties, function (i, item) {
            casualties.push('<li>' + item['casualty'] + '</li>');
        });  // close each()

        // Clear list and populate
        $('#casualties-list li').remove();
        $('#casualties-list').append(casualties.join(''));
    } else {
        $('#casualties-list').css('display', 'none');
        $('.casualties-list-not-enogh-data').css('display', 'block');
    }

    if (data.property.length != 0) {
        $('#property-list').css('display', '');
        $('.property-list-not-enogh-data').css('display', 'none');
        var property = [];
        $.each(data.property, function (i, item) {
            property.push('<li>' + item['property'] + '</li>');
        });  // close each()

        // Clear list and populate
        $('#property-list li').remove();
        $('#property-list').append(property.join(''));
    } else {
        $('#property-list').css('display', 'none');
        $('.property-list-not-enogh-data').css('display', 'block');
    }
    if (data.motivations.length != 0) {
        $('#motivations-list').css('display', '');
        $('.motivations-list-not-enogh-data').css('display', 'none');
        var property = [];
        $.each(data.motivations, function (i, item) {
            property.push('<li>' + item['motivations'] + '</li>');
        });  // close each()

        // Clear list and populate
        $('#motivations-list li').remove();
        $('#motivations-list').append(property.join(''));
    } else {
        $('#motivations-list').css('display', 'none');
        $('.motivations-list-not-enogh-data').css('display', 'block');
    }
}

// Get max json item based on an array of JSON's
function getTopN(arr, prop, n) {
    // clone before sorting, to preserve the original array
    var clone = arr.slice(0);

    // sort descending
    clone.sort(function (x, y) {
        if (x[prop] == y[prop]) return 0;
        else if (parseInt(x[prop]) < parseInt(y[prop])) return 1;
        else return -1;
    });

    return clone.slice(0, n || 1);
}

// Add 2 values
function add(a, b) {
    return a + b;
}

// Populate violence type with the distinct values from the database
function buildViolenceTypeDropDown() {
    // Get violence dropdown options instance
    var violence_options = $("#violence-type-select");
    var url = '/api/' + $('#data-source-select').val() + '/get/violence-types';
    // Get request to get the violence types
    $.get(url, function (data) {
        violence_options.empty();
        $.each(data, function (item) {
            violence_options.append($("<option />").val(data[item]).text(data[item]));
        });
        if ($('#data-source-select').val() == 'idams') {
            $("#violence-type-select").val('Violent Extremism');
            allData = getData(false);
        } else {
            $("#violence-type-select").val('Destruction of property');
            allData = getData(false);
        }
    });
}

// Capitalize a string
function capitalize(s) {
    return s[0].toUpperCase() + s.slice(1);
}
function updateMapValues() {

    var map = $('#map').highcharts(),
        points = map.series[0].points;

    var data = allData['incident-stats'];
    var values_array = {};
    for (var item in data) {
        values_array[data[item]['name'].toString()] = data[item]["incidents"]
    }
    for (var i in points) {

        var val = values_array[points[i].name];
        if (val != undefined) {
            points[i].update({value: val}, false);
            points[i].update({color: mapColor(val)})
        } else {
            points[i].update({value: undefined}, true);
            points[i].update({color: mapColor(0)})
        }
        map.redraw();
    }

}

function mapColor(val) {
    if (val == 0) {
        return "#ffffff"
    }
    if (val <= 10 && val >= 0) {
        return "#a3dbb9"
    }
    if (val > 10 && val <= 20) {
        return "#fbfa20"
    }
    if (val > 20 && val <= 40) {
        return "#f8c733"
    }
    if (val > 40 && val <= 60) {
        return "#feb126"
    }
    if (val > 60 && val <= 100) {
        return "#f7802d"
    }
    if (val > 100 && val <= 150) {
        return "#c56624"
    }
    if (val > 150 && val <= 200) {
        return "#c56626"
    }
    if (val > 200 && val <= 300) {
        return "#ac591f"
    }
    if (val > 300 && val <= 500) {
        return "#944c1b"
    }
    if (val > 500) {
        return "#7b4016"
    }


}
// Build map data series based on the incident number number
function buildDataSeries() {
    var json_data = {};
    var divisions = {};
    var districts = {};
    var upazilas = {};

    for (var item in allData['map-victims-count']['divisions']) {
        divisions[allData['map-victims-count']['divisions'][item]['division'].toString()] = allData['map-victims-count']['divisions'][item]["incidents"]
    }

    for (var item in allData['map-victims-count']['districts']) {
        if (allData['map-victims-count']['districts'][item]['district'] != null && allData['map-victims-count']['districts'][item]['district'] != '') {
            districts[allData['map-victims-count']['districts'][item]['district'].toString()] = allData['map-victims-count']['districts'][item]["incidents"]

        }
    }

    for (var item in allData['map-victims-count']['upazilas']) {
        upazilas[allData['map-victims-count']['upazilas'][item]['upazila']] = allData['map-victims-count']['upazilas'][item]["incidents"]
    }

    json_data['division'] = divisions;
    json_data['district'] = districts;
    json_data['upazila'] = upazilas;
    return json_data;
}
