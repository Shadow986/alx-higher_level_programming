$(document).ready(function() {
    $('#btn_translate').click(function() {
        const lang = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang, function(data) {
            $('#hello').text(data.hello);
        });
    });
    $('#language_code').keypress(function(event) {
        if (event.keyCode === 13) {
            const lang = $('#language_code').val();
            $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang, function(data) {
                $('#hello').text(data.hello);
            });
        }
    });
});
