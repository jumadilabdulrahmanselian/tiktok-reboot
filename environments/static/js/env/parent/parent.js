'use strict';

var ExAsParent = (function() {
    var idTable = "#AsTable";
    var MAIN = 'master/peralatan/';
    var e3nCeL0t = ExAs.base();
    var tableApi, modal_header = '';

    var tb = new DataTable(idTable, {
        "order": [
            [0, 'asc']
        ],
        columnDefs: [{
                targets: [9],
                orderable: false,
            },
            {
                targets: [1, 6, 7, 8],
                visible: false,
                searchable: false
            }
        ],
        "fnInfoCallback": function(oSettings, iStart, iEnd, iMax, iTotal, sPre) {
            $('#tableInfo').html('Menampilkan ' + iStart + " Sampai " + iEnd + " Data Dari " + iTotal + ' Data')
            return iStart + " - " + iEnd + " of " + iTotal;
        },
        drawCallback: function(oSettings) {
            tableApi = this.api()
        }
    })

    var tableCss = function() {
        $(idTable).attr('style', 'margin:0px !important');
    }

    var hideSearch = function() {
        $(idTable + "_filter").hide();
        $(idTable + "_length").hide();
    }

    var hidePagination = function() {
        $(idTable + "_paginate").hide();
        $(idTable + "_info").hide();
    }

    var select2 = function() {
        $('select.select2').each(function() {
            var label = $(this).closest('div')
            label = label.find('label').text()
            label = label.replace('*', '')
            $(this).select2({
                placeholder: "Silahkan Pilih " + label,
                allowClear: true,
                dropdownParent: $(this).closest('.modal')
            });
        });
    }

    var pagination = function() {
        ExAs.Table.Pagination(tableApi)
    }

    var search = () => {
        /**
         * Init All Environment
         */
        hideSearch();
        hidePagination();
        tableCss();

        pagination();
        select2();

        var search = ExAs.Doc.Select("#tableSearch");
        ExAs.Doc.Listen('keyup', function() {
            if (tb.search() !== this.value) {
                tb.search(this.value, true, false).draw();
            }
        }, search)

        var filter = ExAs.Doc.Select("#tableLength");
        ExAs.Doc.Listen('change', function() {
            tb.page.len($(this).val()).draw();
            var page = tb.page.info();
            if (page.pages == 1) {
                $('.previous').attr('disabled', true);
                $('.next').attr('disabled', true);
                $('.existPaginate').val(1)
            } else {
                $('.previous').attr('disabled', true);
                $('.next').removeAttr('disabled');
            }
        }, filter)
    }

    var action_btn = function() {
        return '<div class="input-group">' +
            '<button type="button" class="btn btn-warning btn-icon waves-effect waves-light tombolEdit"><i class="ri-pencil-line"></i></button>' +
            '<button type="button" class="btn btn-danger btn-icon waves-effect waves-light tombolDelete"><i class="ri-delete-bin-5-line"></i></button>' +
            '</div>';
    }

    var is_banned = function(banned) {
        if (!banned) {
            return '<span class="badge badge-soft-success">Active</span>'
        } else {
            return '<span class="badge badge-soft-danger">Banned</span>'
        }
    }

    var is_crawl = function(iscrawl) {
        if (iscrawl) {
            return '<span class="badge badge-soft-success">True</span>'
        } else {
            return '<span class="badge badge-soft-danger">False</span>'
        }
    }

    var is_private = function(isprivate) {
        if (isprivate) {
            return '<span class="badge badge-soft-danger">True</span>'
        } else {
            return '<span class="badge badge-soft-success">False</span>'
        }
    }

    /**
     * Getting Data From Database
     */

    var loadData = () => {
        ExAl.Loading.Table.Show();
        $.ajax({
            url: e3nCeL0t + "admin/parent/load",
            method: "POST",
            async: false,
            data: {
                scrty: true
            },
            success: function(response) {
                ExAl.Loading.Table.Hide();
                var res = response
                if (res.status) {
                    var no = 1;
                    var availableData = []
                    var totalDataExist = 0;
                    var deletedData = []
                    tb.rows().every(function(rowIdx, tableLoop, rowLoop) {
                        var data = this.data();
                        availableData.push(data[1])
                    });

                    totalDataExist = availableData.length

                    $.each(res.data, function(i, item) {
                        var isReady = availableData.includes(item.id_parent);
                        if (isReady === false) {
                            totalDataExist++;
                            tb.row.add([
                                totalDataExist,
                                item.id_parent,
                                item.uname,
                                is_banned(item.is_banned),
                                is_crawl(item.is_crawl),
                                is_private(item.is_private),
                                item.is_banned,
                                item.is_crawl,
                                item.is_private,
                                action_btn()
                            ])
                        } else {
                            tb.rows().every(function(rowIdx, tableLoop, rowLoop) {
                                var data = this.data();
                                if (data[1] == item.id_parent) {
                                    if (data[2] !== item.uname) {
                                        tb.cell(rowIdx, 2)
                                            .data(item.uname)
                                    }

                                    if (data[3] !== is_banned(item.is_banned)) {
                                        tb.cell(rowIdx, 3)
                                            .data(is_banned(item.is_banned))
                                    }

                                    if (data[4] !== is_crawl(item.is_crawl)) {
                                        tb.cell(rowIdx, 4)
                                            .data(is_crawl(item.is_crawl))
                                    }

                                    if (data[5] !== is_private(item.is_private)) {
                                        tb.cell(rowIdx, 5)
                                            .data(is_private(item.is_private))
                                    }

                                    if (data[6] !== item.is_banned) {
                                        tb.cell(rowIdx, 6)
                                            .data(item.is_banned)
                                    }

                                    if (data[7] !== item.is_crawl) {
                                        tb.cell(rowIdx, 7)
                                            .data(item.is_crawl)
                                    }

                                    if (data[8] !== item.is_private) {
                                        tb.cell(rowIdx, 8)
                                            .data(item.is_private)
                                    }

                                    if (data[9] !== action_btn()) {
                                        tb.cell(rowIdx, 9)
                                            .data(action_btn())
                                    }
                                }
                            });
                        }
                        deletedData.push(item.id_parent)
                    })

                    tb.draw(false);

                    $.each(availableData, function(i, item) {
                        var isDeleted = deletedData.includes(availableData[i]);
                        var indexes = availableData.indexOf(availableData[i]);
                        if (isDeleted === false) {
                            tb.row(indexes).remove().draw();
                        }
                    })
                } else {
                    tb.clear().draw();
                }
            }
        })
    }

    /**
     * Transaction
     */

    var Transaction = function() {
        addTrigger();
        updateTrigger();
        updateClickTrigger();
        deleteTrigger();
    }

    var addTrigger = function() {
        if (ExAs.Doc.Exist("#form_tambah")) {

            ExAs.Validator("#submit", function(isValid) {
                var _input = $("#form_tambah").serializeArray();
                _input.push({ name: "scrty", value: true })

                $(this).addClass("spinner spinner-white spinner-right disabled");
                $("#form_tambah button").attr("disabled", "disabled");

                if (isValid == true) {
                    $.ajax({
                        url: e3nCeL0t + MoDaD + MAIN + "add",
                        method: "POST",
                        data: $.param(_input),
                        success: function(response) {
                            $("#submit").removeClass("spinner spinner-white spinner-right disabled");
                            $("#form_tambah button").removeAttr("disabled");

                            if (ExAs.Utils.Json.valid(response)) {
                                var res = JSON.parse(response);
                                if (res.status) {
                                    ExAl.Toast.Success(res.header, res.message, function(result) {
                                        if (result.isDismissed) {
                                            loadData();
                                            ExAl.Modal.Close('#modalTambah', true);
                                            $('#form_tambah').trigger('reset')
                                        }
                                    });
                                } else {
                                    ExAl.Toast.Failed(res.header, res.message);
                                }
                            }
                        },
                        error: function(e) {
                            // console.log(e);
                            $("#submit").removeClass("spinner spinner-white spinner-right disabled");
                        },
                    });
                } else {
                    $("#submit").removeClass("spinner spinner-white spinner-right disabled");
                    $("#form_tambah button").removeAttr("disabled");
                }
            });
        }
    };

    var updateClickTrigger = function() {
        $("table tbody").on("click", ".tombolEdit", function() {
            var drop = tb.row($(this).parents("tr")).data();
            if (modal_header == '') {
                modal_header = $('#modal_header_edit').text();
            }
            $('#modal_header_edit').html(modal_header + ' : <b>' + drop[2] + '</b>');
            $('#id_parent').val(drop[1]);
            $('#username_edit').val(drop[2]);
            $('#banned_edit').val(drop[3]);
            $('#crawl_edit').val(drop[4]);
            $('#private_edit').val(drop[5]);
            ExAl.Modal.Show('#modalEdit');
        });
    }

    var updateTrigger = function() {
        if (ExAs.Doc.Exist("#form_edit")) {

            ExAs.Validator("#submitEdit", function(isValid) {
                if (isValid == true) {
                    updateTrigger();
                    var _input = $("#form_edit").serializeArray();
                    _input.push({ name: "scrty", value: true })

                    $(this).addClass("spinner spinner-white spinner-right disabled");
                    $("#form_edit button").attr("disabled", "disabled");

                    $.ajax({
                        url: e3nCeL0t + MoDaD + MAIN + "edit",
                        method: "POST",
                        data: $.param(_input),
                        success: function(response) {
                            $("#submitEdit").removeClass("spinner spinner-white spinner-right disabled");
                            $("#form_edit button").removeAttr("disabled");

                            if (ExAs.Utils.Json.valid(response)) {
                                var res = JSON.parse(response);
                                $('#modal_header_edit').html(modal_header);
                                if (res.status) {
                                    ExAl.Toast.Success(res.header, res.message, function(result) {
                                        if (result.isDismissed) {
                                            loadData();
                                            ExAl.Modal.Close('#modalEdit', true);
                                            $('#form_edit').trigger('reset')
                                        }
                                    });
                                } else {
                                    ExAl.Toast.Failed(res.header, res.message);
                                }
                            }
                        },
                        error: function(e) {
                            // console.log(e);
                            $("#submit").removeClass("spinner spinner-white spinner-right disabled");
                        },
                    });
                } else {
                    $("#submitEdit").removeClass("spinner spinner-white spinner-right disabled");
                    $("#form_edit button").removeAttr("disabled");
                }
            });
        }
    }

    var deleteTrigger = function() {
        $("table tbody").on("click", ".tombolDelete", function() {
            var drop = tb.row($(this).parents("tr")).data();
            ExAl.Toast.Delete({}, function(result) {
                if (result) {
                    $.ajax({
                        url: e3nCeL0t + MoDaD + MAIN + "delete",
                        method: "POST",
                        async: false,
                        data: {
                            id: drop[1],
                            scrty: true
                        },
                        success: function(response) {
                            if (ExAs.Utils.Json.valid(response)) {
                                var res = JSON.parse(response);
                                if (res.status) {
                                    ExAl.Toast.Success(res.header, res.message + ' : <b>' + drop[2] + '</b>');
                                } else {
                                    ExAl.Toast.Failed(res.header, res.message);
                                }
                            }
                        }
                    })
                }
            })
        });
    }

    return {
        run: function() {
            search();
            loadData();
            Transaction();

            setInterval(loadData, GLOBAL_COOLDOWN)
        },
        refresh: function() { loadData() }
    }
})();

var ExAsFresh = ExAsParent;
ExAs.Dom(ExAsParent.run())