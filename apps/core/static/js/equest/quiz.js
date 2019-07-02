// Chamada do metodo cadastrar_disciplina
$('#adicionar-disciplina').click(function(e) {
    Swal.fire({
        title: 'Digite o nome da disciplina',
        input: 'text',
        inputAttributes: {
        autocapitalize: 'off'
        },
        showCancelButton: true,
        showLoaderOnConfirm: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '<i class="fa fa-check"></i> Salvar!',
        cancelButtonText: '<i class="fa fa-times"></i> Cancelar',
        inputValidator: (value) => {
            if (!value) {
                return 'Preencha o nome da disciplina!'
            }
        },
        preConfirm: (value) => {
            //token de sessao
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                headers : {'X-CSRFToken': csrftoken},
                type    : 'POST',
                url     : '/quiz/cadastrar_disciplina/',
                data    : {'nome':value},
                datatype: 'json',

                success: function(data) {
                    if(data.status == "OK"){
                        Swal.fire({
                            position: 'center',
                            type: 'success',
                            title: 'Disciplina cadastrada com sucesso',
                            showConfirmButton: false,
                            timer: 2500
                        })
                        window.setTimeout(function(){ 
                            location.reload();
                        } ,2500);
                        // document.location = data.url_retorno;
                    }
                },
                error: function(data){
                    alert('deu erro');
                }
            });
        },
    })
});

// Metodo de cadastro de disciplina
$('.editar-disciplina').click(function(e) {
    var uuid_disciplina, titulo_disciplina;
    uuid_disciplina = $(this).attr("cs-id");
    titulo_disciplina = $(this).attr("cs-titulo");

    Swal.fire({
        title: 'Editando disciplina',
        input: 'text',
        inputValue: titulo_disciplina,
        inputAttributes: {
        autocapitalize: 'off'
        },
        showCancelButton: true,
        showLoaderOnConfirm: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '<i class="fa fa-check"></i> Salvar!',
        cancelButtonText: '<i class="fa fa-times"></i> Cancelar',
        inputValidator: (value) => {
            if (!value) {
                return 'Preencha o nome da disciplina!'
            }
        },
        preConfirm: (value) => {
            //token de sessao
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                headers : {'X-CSRFToken': csrftoken},
                type    : 'POST',
                url     : "/quiz/editar_disciplina/",
                data    : {"titulo":value, "uuid_disciplina": uuid_disciplina},
                datatype: 'json',

                success: function(data) {
                    if(data.status == "OK"){
                        Swal.fire({
                            position: 'center',
                            type: 'success',
                            title: 'Disciplina editada com sucesso',
                            showConfirmButton: false,
                            timer: 2500
                        })
                        window.setTimeout(function(){ 
                            location.reload();
                        } ,2500);
                    }
                },
                error: function(data){
                    alert('deu erro');
                }
            });
        },
    })
});

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