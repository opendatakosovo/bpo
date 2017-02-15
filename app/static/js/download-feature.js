   $(document).ready(function () {

        national_death_states = [];
        national_death_data_series_array = [];

        national_injury_states = [];
        national_injury_data_series_array = [];

        national_property_damage_states = [];
        national_property_damage_data_series_array = [];

        var main_modal_chart = Highcharts.chart('main-modal-chart', {

            chart: {
                type: 'bar'
            },

            title: {
                text: "",
                align: 'left'
            },

            credits: {
                enabled: false
            },

            xAxis: {
                categories: [],
            },

            yAxis: {
                allowDecimals: false,
                title: {
                    text: null
                },
                min: 0,
                opposite: true
            },


            legend: {
                enabled: false
            },

            series: [{
                name: '',
                data: []
            }]

        });
        var first_modal_chart = Highcharts.chart('first-modal-chart', {

            chart: {
                type: 'bar'
            },

            title: {
                text: "",
                align: 'left'
            },

            credits: {
                enabled: false
            },

            xAxis: {
                categories: [],
            },

            yAxis: {
                allowDecimals: false,
                title: {
                    text: null
                },
                min: 0,
                opposite: true
            },


            legend: {
                enabled: false
            },

            series: [{
                name: '',
                data: []
            }]

        });
        var second_modal_chart = Highcharts.chart('second-modal-chart', {

            chart: {
                type: 'bar'
            },

            title: {
                text: "",
                align: 'left'
            },

            credits: {
                enabled: false
            },

            xAxis: {
                categories: [],
            },

            yAxis: {
                allowDecimals: false,
                title: {
                    text: null
                },
                min: 0,
                opposite: true
            },


            legend: {
                enabled: false
            },

            series: [{
                name: 'Erik',
                data: [3, 6, 1, 2, 6]
            }]

        });
        var third_modal_chart = Highcharts.chart('third-modal-chart', {

            chart: {
                type: 'bar'
            },

            title: {
                text: "",
                align: 'left'
            },

            credits: {
                enabled: false
            },

            xAxis: {
                categories: [],
            },

            yAxis: {
                allowDecimals: false,
                title: {
                    text: null
                },
                min: 0,
                opposite: true
            },


            legend: {
                enabled: false
            },

            series: [{
                name: '',
                data: []
            }]

        });

        $('.download').click(function () {

            $('.first-violence-place').text(allData['incident-stats'][0]['name']);
            var show_specific_charts = false;
            if (allData != undefined && allData['stats'] != undefined) {
                var show_specific_charts = true;
            }


            if (show_specific_charts == true) {
                first_modal_chart = undefined;
                second_modal_chart = undefined;
                third_modal_chart = undefined;
            }

            general_stats = [];
            general_categories = [];

            death_states = [];
            death_data_series_array = [];

            injury_states = [];
            injury_data_series_array = [];

            property_damage_states = [];
            property_damage_data_series_array = [];

            if (allData['incident-stats'].length > 0) {
                $.each(allData['incident-stats'], function (item) {
                    general_stats.push(allData['incident-stats'][item]['incidents']);
                    general_categories.push(allData['incident-stats'][item]['name']);
                });
            }
            if (allData['stats']['death'] != undefined) {
                $.each(allData['stats']['death'], function (item) {
                    death_states.push(allData['stats']['death'][item]['name']);
                    death_data_series_array.push(allData['stats']['death'][item]['total']);
                });
            }

            if (allData['stats']['injury'] != undefined) {
                $.each(allData['stats']['injury'], function (item) {
                    injury_states.push(allData['stats']['injury'][item]['name']);
                    injury_data_series_array.push(allData['stats']['injury'][item]['total']);
                });

            }

            if (allData['stats']['property'] != undefined) {
                $.each(allData['stats']['property'], function (item) {
                    property_damage_states.push(allData['stats']['property'][item]['name']);
                    property_damage_data_series_array.push(allData['stats']['property'][item]['total']);
                });
            }
            $.each(Highcharts.charts, function (item) {
                if (Highcharts.charts[item].renderTo.id == 'main-modal-chart') {
                    $.each(Highcharts.charts[item].series, function (index) {
                        var name = Highcharts.charts[item].series[index].name;
                        Highcharts.charts[item].series[0].setData(general_stats);
                        Highcharts.charts[item].xAxis[0].setCategories(general_categories);
                    });
                    Highcharts.charts[item].redraw();
                } else if (Highcharts.charts[item].renderTo.id == 'first-modal-chart') {
                    $.each(Highcharts.charts[item].series, function (index) {
                        var name = Highcharts.charts[item].series[index].name;
                        Highcharts.charts[item].series[0].setData(death_data_series_array);
                        Highcharts.charts[item].xAxis[0].setCategories(death_states);
                    });
                    Highcharts.charts[item].redraw();
                } else if (Highcharts.charts[item].renderTo.id == 'second-modal-chart') {
                    $.each(Highcharts.charts[item].series, function (index) {
                        var name = Highcharts.charts[item].series[index].name;
                        Highcharts.charts[item].series[0].setData(injury_data_series_array);
                        Highcharts.charts[item].xAxis[0].setCategories(injury_states);
                    });
                    Highcharts.charts[item].redraw();
                } else if (Highcharts.charts[item].renderTo.id == 'third-modal-chart') {
                    $.each(Highcharts.charts[item].series, function (index) {
                        var name = Highcharts.charts[item].series[index].name;
                        Highcharts.charts[item].series[0].setData(property_damage_data_series_array);
                        Highcharts.charts[item].xAxis[0].setCategories(property_damage_states);
                    });
                    Highcharts.charts[item].redraw();
                }
            });
        });

    });
