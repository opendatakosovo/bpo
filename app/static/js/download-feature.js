$(document).ready(function () {
    var idams_disclaimer =
        `The Online Media Review is a geospatial and actor-based database that contains incident information pertaining to the level of political violence, terrorism, safety and security, and natural and human-induced hazards in Bangladesh. The database is populated daily using openly  available information published by the online media both in English and Bangla. The pilot dataset presented in the Bangladesh Peace Observatory Platform covers the time period of June 2015 - August 2016. 

The database consists of a number of layers of information pertaining to each incident reported in the online media;  types, triggers or motivations, consequences for each incident (such as death, injury and property damages), actors, and sources. The publication of the data is for pilot purposes, and there may be errors in data collection, validation and/or reporting by the media. 

For the purpose of this pilot database project, the following online media have been reviewed: thedailystar.net; Banglanews24.com; bdnews24.com; Daily-sun.com; dhakatribune.com; thefinancialexpress-bd.com.Other online media reviewed with less frequency are en.prothom-alo.com; thereport24.com; risingbd.com; and unb.com.bd.

The database relies on the following definitions: 
    1.  Political Violence: 1) violence: includes an incident that results in at least one death, or 
        property destruction,  2) political – involving members of at least one clearly defined 
        political group, public institution and/or civil society, interest groups, Islamist 
        organizations, rebel and  militant groups (Suykens and Islami, 2015). Political groups 
        include political parties and all their allied  organizations such as volunteer, youth and 
        worker groups.
    2.  Terrorism and radicalism: includes incidents involving Islamist organizations, rebel and militant 
        groups (non-political party) who use violence and intimidation for political or religious aims, 
        and in many cases are proscribed by the government as terrorist groups.
    3.  Safety and security – incidents related to 1) security and crime, or other forms of homicide which
        includes non-politically motivated crimes such as robbery and theft, vandalism, etc.
Within these domains, the BPO presents the following incident categories under the Online Media Review :

    1.  Political Dispute: Any violent confrontation involving members of same or different political party/groups.
    
    2.  Terrorism and radicalism: includes incidents involving Islamist  organizations, rebel and militant 
        groups (non-political party) who use violence and intimidation for political or religious aims, and 
        in many cases are proscribed by the government as terrorist groups.
    
    3.  Border Incidents: Actions taken by law enforcement or armed forces entities  (of India, Myanmar or 
        Bangladesh) which may lead to arrests
        
    `

    var idams_disclaimer_page_2 = `
    4.  Arson Attack: is the crime of intentionally and maliciously setting fire to buildings, wildland 
        areas, dumpsters, vehicles or other property with the intent to cause damage.
    
    5.  IED Attack: involves attacks with any non-conventional made explosives like petrol bomb, suicide 
        vest bombing, cotail and grenade attacks, etc. 
    
    6.  Mob Violence: Indicates when more than two or more community members take the law on their hands
        and punish people for wrongdoing. Mob violence in Bangladesh often leads to violent death of 
        people who were caught doing misdeeds in the community (theft, etc)
    
    7.  Violent Crime/Homicides: A violent action that leads to the death or injury of a person or in 
        which lethal weapons. The incidents that are associated with murder, honour Killing, mob violence, 
        armed robbery, clashes among gangs, etc
    `


    var mgr_disclaimer =
        `
    The Print Media Review Database (PMRD) identifies and codes events of political violence in Bangladesh from print media content analysis. The aim of the PMRD database is to capture to the best possible extent of as many instances and reliable information pertaining to political violence incidents in the country. The PMRD is managed by the Microgovernance Research Institute (MGR) at University of Dhaka, and covers political violence incidents for the period of 2014 – 2016.
     
    Events have been coded from four different national printed newspapers: Daily Star, Inqilab, Ittefaq and Prothom Alo. 
    They have been chosen for a combination of circulation, reputation, ideological position, network of correspondents and language. All newspapers have regional correspondents, often up to the Upazila, or Union level, enabling them to cover a wide range of local events. To be included in the database a coded event must be 
    1) violent: resulting in at least one injured/ death/raped/abducted/held hostage or in property destruction and 
    2) explicitly political: involving members of at least one clearly delineated political group: political party and all its allied organizations, Islamist organization, or rebel group. A violent event is coded as a single event if: 
        1) It takes place on the same day 
        2) It takes place at the same place, 
        3) It involves the same actor (if only one actor is involved) or at least two of the same actors throughout.
     
                                 Coding, variables and post processing
    Coding in the PMRD is based on a detailed codebook, listing the different variables, and codes to denote
    specific places up to sub-districts, diverse actors, types of violence, range of violence trigger, 
    human impact, property destructions,, etc.  The codebook aimed at minimizing interpretation of reports 
    by the data analysts. The DAs have been recruited from Dhaka University students focusing on their 
    capacity building. 
    They have gone through several intensive training workshops, exercise session and piloting before 
    they finally start the reading and entries.  DAs are assigned a specific newspaper and a specific time 
    period, rotating between newspapers after every three-month period. 
    The PMRD is a compressive database covering diverse range of actors, violence categories, determinants, 
    triggers and consequences. However, Bangladesh Peace Observatory (BPO) platform covers following 
    political violence categories.  
     
    1.  Political clash/attack: Violent clashes/battle and attack in which actors from general political 
        parties, affiliated organizations, identity groups and alliances are directly involved and define the 
        fighting and violence. It covers both intra-party clashes and inter-party attacks. 
`
    var mgr_disclaimer_page_2 = `
    2.  Violent extremism (Islamist): Political violence perpetrated by the Islamists radical outfits around 
        the country with political and religious aims. It includes incidences of attack and killing online 
        activists, bloggers, foreigners, atheists, and sufists around the country.  
    3.  Violent extremism (Rebel): Political violence perpetrated by ultra-left ideological groups and ethnic 
        rebels around the country. 
    4.  Electoral violence: Political violence between different actors related to elections at local, 
        regional and national levels. It includes elections as the direct trigger or direct cause of the 
        violent event. 
    5.  Hartal violence: Political violence incidences as part of a clearly mentioned hartal day(s). 
    6.  Destruction of property (Excluding arson attack): Destruction of property, including moveable goods, 
        excluding burning.
    7.  Arson attack: Destruction of property, including moveable goods by burning/throwing petrol bomb.
    8.  High and low impact bombing: Setting off an explosive device (e.g. cocktail, car bomb) causing 
        or aimed to cause small to large-scale destruction or casualties.
    9.  Abduction, kidnap, hostage and rape: Kidnapping, abduction and hostage indicates that the captive is 
        held at the same or unknown locations. Rape is conducting any sexual activities against at least one of 
        the participants’ will.
    10. Other types of political violence: This category includes incidences in which actors or perpetrators 
        are unspecified or not mentioned.
        
    Using newspapers as a data source is potentially controversial. Yet there are limited other data sources providing 
    wide ranging coverage of events. While watchdog institutions like Freedom House are critical of press freedom in 
    Bangladesh, they also state that print media is given relatively more scope to publish freely (Freedom House 2015). 
    A number of caveats and safeguards apply to accurately interpret the results under PMRD database. 
    First, quite narrow definition of political violence was taken, focusing on ‘organisational’ violence. This is to 
    minimize the interpretation of what connotes ‘political’. 
    Second, our estimates for lethal casualties and wounded are expected to be conservative. The coding protocol 
    specifies that, in the case of uncertainty, the lowest possible number should be recorded.
    Third, we have a regional bias by using the Dhaka editions of our four newspapers. Three of the newspapers have 
    regional editions that include additional news about a specific region. 
`

    national_death_states = [];
    national_death_data_series_array = [];

    national_injury_states = [];
    national_injury_data_series_array = [];

    national_property_damage_states = [];
    national_property_damage_data_series_array = [];

    var main_modal_chart = Highcharts.chart('main-modal-chart', {

        chart: {
            type: 'bar',
            renderTo: "main-modal-chart",
            height: 262,
            width: 625,
            description: "Ranking of locations based on number of incidents."
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
        navigator: {
            series: {
                includeInCSVExport: false
            }
        },
        series: [{
            name: 'Incidents',
            data: []
        }],
        exporting: {
            csv: {
                dateFormat: '%Y-%m-%d'
            }
        }

    });
    var first_modal_chart = Highcharts.chart('first-modal-chart', {

        chart: {
            type: 'bar',
            renderTo: "first-modal-chart",
            height: 262,
            width: 625,
            description: "Ranking of locations based on number of deaths."
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
        navigator: {
            series: {
                includeInCSVExport: false
            }
        },
        series: [{
            name: 'Deaths',
            data: []
        }],
        exporting: {
            csv: {
                dateFormat: '%Y-%m-%d'
            }
        }

    });
    var second_modal_chart = Highcharts.chart('second-modal-chart', {

        chart: {
            type: 'bar',
            renderTo: "second-modal-chart",
            height: 262,
            width: 625,
            description: "Ranking of locations based on number of injuries."
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
        navigator: {
            series: {
                includeInCSVExport: false
            }
        },
        series: [{
            name: 'Injuries',
            data: [3, 6, 1, 2, 6]
        }],
        exporting: {
            csv: {
                dateFormat: '%Y-%m-%d'
            }
        }

    });
    var third_modal_chart = Highcharts.chart('third-modal-chart', {

        chart: {
            type: 'bar',
            renderTo: "third-modal-chart",
            height: 262,
            width: 625,
            description: "Ranking of property damages based on location."
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
        navigator: {
            series: {
                includeInCSVExport: false
            }
        },
        series: [{
            name: 'Property Damage',
            data: []
        }],
        exporting: {
            csv: {
                dateFormat: '%Y-%m-%d'
            }
        }

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
            if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'main-modal-chart') {
                $.each(Highcharts.charts[item].series, function (index) {
                    var name = Highcharts.charts[item].series[index].name;
                    Highcharts.charts[item].series[0].setData(general_stats);
                    Highcharts.charts[item].xAxis[0].setCategories(general_categories);
                });
                Highcharts.charts[item].redraw();
            } else if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'first-modal-chart') {
                $.each(Highcharts.charts[item].series, function (index) {
                    var name = Highcharts.charts[item].series[index].name;
                    Highcharts.charts[item].series[0].setData(death_data_series_array);
                    Highcharts.charts[item].xAxis[0].setCategories(death_states);
                });
                Highcharts.charts[item].redraw();
            } else if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'second-modal-chart') {
                $.each(Highcharts.charts[item].series, function (index) {
                    var name = Highcharts.charts[item].series[index].name;
                    Highcharts.charts[item].series[0].setData(injury_data_series_array);
                    Highcharts.charts[item].xAxis[0].setCategories(injury_states);
                });
                Highcharts.charts[item].redraw();
            } else if (Highcharts.charts[item] != undefined && Highcharts.charts[item].renderTo.id == 'third-modal-chart') {
                $.each(Highcharts.charts[item].series, function (index) {
                    var name = Highcharts.charts[item].series[index].name;
                    Highcharts.charts[item].series[0].setData(property_damage_data_series_array);
                    Highcharts.charts[item].xAxis[0].setCategories(property_damage_states);
                });
                Highcharts.charts[item].redraw();
            }
        });

        $('#Story_Frame_Aggregated_Data_Download').click(function () {
            var csv_data = [];
            var csv_data1 = [];
            var csv_data2 = [];
            var csv_data3 = [];

            $.each(Highcharts.charts, function (item) {
                if (Highcharts.charts[item].renderTo.id == 'main-modal-chart') {
                    csv_data = Highcharts.charts[item].getCSV().split(/\r?\n/);
                } else if (Highcharts.charts[item].renderTo.id == 'first-modal-chart') {
                    csv_data1 = Highcharts.charts[item].getCSV().split(/\r?\n/);

                } else if (Highcharts.charts[item].renderTo.id == 'second-modal-chart') {
                    csv_data2 = Highcharts.charts[item].getCSV().split(/\r?\n/);
                } else if (Highcharts.charts[item].renderTo.id == 'third-modal-chart') {
                    csv_data3 = Highcharts.charts[item].getCSV().split(/\r?\n/);
                }
            });
            var data_array = [];
            $.each(csv_data1, function (index, item) {
                if (index == 0) {
                    var line = item.split(',');
                    var name = "Location";
                    line.unshift(name);
                    data_array.push(line);
                } else {
                    var line = item.split(',');
                    var name = getName();
                    line.unshift(name);
                    data_array.push(line);
                }

            })


            $.each(csv_data2, function (index, item) {
                var line = item.split(',');
                data_array[index].push(line[1])

            })

            $.each(csv_data3, function (index, item) {
                var line = item.split(',');
                data_array[index].push(line[1] + "\r")
            })
            data_array = data_array.map(function (d) {
                return d.join();
            }).join('\n');
            download('Story_Frame_Data.csv', data_array);
        });

        $('#Story_Frame_Raw_Download').click(function () {

            data_array = Papa.unparse(allData['raw-incident-stats']);
            download('Story_Frame_Data.csv', data_array);
        });

        $('#Story_Frame_PDF_Download').click(function () {
            var today = new Date();
            var month = new Array();
            month[0] = "January";
            month[1] = "February";
            month[2] = "March";
            month[3] = "April";
            month[4] = "May";
            month[5] = "June";
            month[6] = "July";
            month[7] = "August";
            month[8] = "September";
            month[9] = "October";
            month[10] = "November";
            month[11] = "December";
            var dd = today.getDate();
            var mm = today.getMonth() + 1; //January is 0!
            var yyyy = today.getFullYear();
            var date = month[mm-1] + " " + dd + ", " + yyyy;
            // Generate PDF
            options = {
                orientation: "p",
                unit: "pt",
                format: "a4",
                lineHeight: 1.5
            };
            var dataset = $('#data-source-select').val();

            var lMargin = 50; //left margin in mm
            var rMargin = 0; //right margin in mm
            var pdfInMM = 660;  // width of A4 in mm
            var doc = new jsPDF(options);
            // Optional - set properties on the document
            doc.setProperties({
                title: 'BPO Analytics',
                subject: 'BPO Analytics',
                author: '',
                keywords: '',
                creator: 'Partin Imeri'
            });
            var x = 40;


            var document_width = doc.internal.pageSize.width;
            var document_height = doc.internal.pageSize.height;
            doc.addFont("Roboto Slab", "Roboto Slab", "normal");
            doc.setFont("Roboto Slab", 'normal');
            doc.setLineWidth(document_width);

            if (dataset == 'idams') {
                // Add disclaimer title (above the line)
                doc.setFontSize(14);
                var disclaimer_title = 'Disclaimer: The Online Media Review Database';
                var disclaimerXOffset = (doc.internal.pageSize.width / 2) - (doc.getStringUnitWidth(disclaimer_title) * doc.internal.getFontSize() / 2);
                doc.text(disclaimerXOffset, 50, disclaimer_title);
            } else {
                // Add disclaimer title (above the line)
                doc.setFontSize(14);
                var disclaimer_title = 'Disclaimer: The Print Media Review Database';
                var disclaimerXOffset = (doc.internal.pageSize.width / 2) - (doc.getStringUnitWidth(disclaimer_title) * doc.internal.getFontSize() / 2);
                doc.text(disclaimerXOffset, 50, disclaimer_title);
            }
            // Add line
            doc.setLineWidth(0.5);
            doc.line(50, 60, document_width - 50, 60);

            // Add document title
            doc.setFontSize(22);
            var document_title = 'The Bangladesh Peace Observatory';
            var titleOffset = (doc.internal.pageSize.width / 2) - (doc.getStringUnitWidth(document_title) * doc.internal.getFontSize() / 2);
            doc.text(titleOffset, 120, document_title);

            // Add date
            doc.setFontSize(14);
            var datexOffset = (doc.internal.pageSize.width / 2) - (doc.getStringUnitWidth(date) * doc.internal.getFontSize() / 2);
            doc.text(datexOffset, 170, date);

            if (dataset == 'mgr') {
                // Add MGR Disclaimer text
                var lines = doc.splitTextToSize(mgr_disclaimer, (pdfInMM - lMargin - rMargin));
                doc.setFontSize(11);
                doc.text(lMargin, 190, lines);
                doc.addPage();

                // Add MGR second page.
                var lines = doc.splitTextToSize(mgr_disclaimer_page_2, (pdfInMM - lMargin - rMargin));
                doc.setFontSize(11);
                doc.text(lMargin, 50, lines);
                doc.addPage();
            } else {
                // Add IDAMS Disclaimer text
                var lines = doc.splitTextToSize(idams_disclaimer, (pdfInMM - lMargin - rMargin));
                doc.setFontSize(11);
                doc.text(lMargin, 190, lines);
                doc.addPage();

                var lines = doc.splitTextToSize(idams_disclaimer_page_2, (pdfInMM - lMargin - rMargin));
                doc.setFontSize(11);
                doc.text(lMargin, 50, lines);
                doc.addPage();
            }


            $.each(Highcharts.charts, function (item) {

                if (Highcharts.charts[item] != undefined) {
                    var id = Highcharts.charts[item].renderTo.id;

                    var imgData = convertSVGtoPDF(Highcharts.charts[item].getSVG(), id, document_width);

                    var width = $('#' + id).children().children()[0].getBBox().width;
                    var height = $('#' + id).children().children()[0].getBBox().height;


                    doc.addImage(imgData, 'JPEG', 80, 90, width - 90, height - 50);

                    if ($('.' + id).length > 0) {
                        var text = $('.' + id).text().trim().replace(/ {2,}/, ' ').replace('\n', ' ');
                        doc.text(document_width / 5, 70, text);
                    }
                    doc.text(document_width / 6, document_height - 50, 'Description: ' + Highcharts.charts[item].options.chart.description);
                    doc.addPage();
                }

            });
            var data_array = Papa.unparse(allData['raw-incident-stats']);
            var data_table_array = data_array.split('\n');
            var columns = data_table_array[0].split(',');
            var rows = [];
            $.each(data_table_array, function (index, item) {
                if (index > 0) {
                    rows.push(item.split(','));
                }
            })
            doc.save('BPO Analysis.pdf');
        });
        function convertSVGtoPDF(svg, id, document_width) {
            var width = $('#' + id).children().children()[0].getBBox().width;
            var height = $('#' + id).children().children()[0].getBBox().height;
            // create canvas
            var canvas = document.createElement("canvas");
            if (height > 0) {
                canvas.height = height;
            } else {
                canvas.height = 180;
            }
            if (width > 0 || width > 1000) {
                canvas.width = width + 100;
            } else {
                canvas.width = document_width + 50;
            }
            canvas.background = "#fff"
            // make it base64
            var svg64 = btoa(unescape(encodeURIComponent(svg)));
            var b64Start = 'data:image/svg+xml;base64,';

            // prepend a "header"
            var image64 = b64Start + svg64;
            var img = new Image();
            img.src = image64;
            img.style = "background-color:white;"

            // draw the image onto the canvas
            var ctx = canvas.getContext('2d');
            ctx.drawImage(img, 0, 0);
            // change non-opaque pixels to white
            var imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            var data = imgData.data;
            for (var i = 0; i < data.length; i += 4) {
                if (data[i + 3] < 255) {
                    data[i] = 255;
                    data[i + 1] = 255;
                    data[i + 2] = 255;
                    data[i + 3] = 255;
                }
            }
            ctx.putImageData(imgData, 0, 0);

            var imgData_ = canvas.toDataURL('image/jpeg');
            return imgData_;

        }


    });


});
