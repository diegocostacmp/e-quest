function temporizador(){
    setInterval(function() { console.log("setInterval: Ja passou 1 segundo!"); }, 1000);    
}
temporizador();



 // using jQuery to generate csrf_token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// New game 
$('#game-create').click(function() {
    bookGame();
});

function bookGame(){
    //token de sessao
    var csrftoken = getCookie('csrftoken');

     // Get data select
    $.ajax({
        headers : {'X-CSRFToken': csrftoken},
        type    : 'POST',
        url     : $("#game-create").attr("eg-url"),

        success: function(data) {
            var options = {};

            $.map(data,
                function(o){
                    options[o.uuid] = o.discipline;
                });

            const {value: opt} = Swal.fire({
                title: 'Selecione uma disciplina',
                input: 'select',
                inputOptions: options,
                inputPlaceholder: 'Selecione uma disciplina',
                inputAttributes: {
                autocapitalize: 'off'
                },
                showCancelButton: true,
                showLoaderOnConfirm: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: '<i class="fa fa-check"></i> Buscar!',
                cancelButtonText: '<i class="fa fa-times"></i> Cancelar',
                inputValidator: (value) => {
                    if (!value) {
                        return 'Selecione uma disciplina!'
                    }
                },
                preConfirm: (value) => {
                    window.location = '/game/game_create/'+value+'/';
                },
            })

        },
        error: function(){
            alert('deu erro');
        }
    });
    
}


