function login(thos) {
    var data = $('#form').serializeArray()
        // var e3nCeL0t = ExAs.uXvbI(uXvbI);
    var e3nCeL0t = ExAs.base();
    data.push({
        name: "scrty",
        value: true
    })

    $(thos).attr('disabled', true)
    $(thos).find('.auth-loading').css('display', 'inline-block')

    $.ajax({
        url: e3nCeL0t + "auth/authorize",
        data: data,
        method: "POST",
        success: function(response) {
            var x = response
            $(thos).removeAttr('disabled')
            $(thos).find('.auth-loading').css('display', 'none')
            if (x.status) {
                Swal.fire({
                    html: '<div class="mt-3"><lord-icon src="https://cdn.lordicon.com/lupuorrc.json" trigger="loop" colors="primary:#0ab39c,secondary:#405189" style="width:120px;height:120px"></lord-icon><div class="mt-4 pt-2 fs-15"><h4>' + x.header + '</h4><p class="text-muted mx-4 mb-0">' + x.message + '</p></div></div>',
                    showCancelButton: !1,
                    showConfirmButton: !1,
                    timer: 2000
                }).then((result) => {
                    if (result.isDismissed) {
                        window.location = e3nCeL0t + "admin/dashboard"
                    }
                })
            } else {
                Swal.fire({
                    html: '<div class="mt-3"><lord-icon src="https://cdn.lordicon.com/tdrtiskw.json" trigger="loop" colors="primary:#f06548,secondary:#f7b84b" style="width:120px;height:120px"></lord-icon><div class="mt-4 pt-2 fs-15"><h4>' + x.header + '</h4><p class="text-muted mx-4 mb-0">' + x.message + '</p></div></div>',
                    showCancelButton: !1,
                    showConfirmButton: !1,
                    timer: 3000
                })
            }
        }
    });
}

$('#form').on('keypress', function(e) {
    if (e.which == 13) {
        login()
    }
});