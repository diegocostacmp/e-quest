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

$('.excluir-quiz').click(function(e) {
    var url_destino, uuid_editando;
    url_destino = $(this).attr('cs-url');
    uuid_editando = $(this).attr('cs-id');

    Swal.fire({
        title: 'Tem certeza que deseja excluir?',
        text: "Esta ação não pode ser desfeita!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '<i class="fa fa-check"></i> Sim, quero!',
        cancelButtonText: '<i class="fa fa-times"></i> Não, Cancelar',
        preConfirm: (value) => {
            //token de sessao
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                headers : {'X-CSRFToken': csrftoken},
                type    : 'POST',
                url     : String(url_destino),
                data    : {'uuid_editando':uuid_editando},
                datatype: 'json',

                success: function(data) {
                    if(data.status == "OK"){
                        Swal.fire(
                            'Deleted!',
                            'Cadastro excluído com sucesso.',
                            'success'
                        )
                        window.setTimeout(function(){ 
                            location.reload();
                        } ,1000);
                    }
                },
                error: function(){
                    Swal.fire({
                        type: 'error',
                        title: 'Desculpe...',
                        text: 'Existem dependências associadas!'
                    })
                }
            });
        },
    })
})


// Adicionar Quizzes
$('#adicionar-quizzes').click(function(e) {

    // Get uuid disciplina
    var disciplina = $('#disciplina-uuid').val();
    console.log(disciplina);

    Swal.fire({
        title: 'Digite o nome do quiz',
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
                return 'Preencha o nome do quiz!'
            }
        },
        preConfirm: (value) => {
            //token de sessao
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                headers : {'X-CSRFToken': csrftoken},
                type    : 'POST',
                url     : '/quiz/cadastrar_quiz/',
                data    : {
                    'nome': value,
                    'disciplina': disciplina} ,
                datatype: 'json',

                success: function(data) {
                    if(data.status == "OK"){
                        Swal.fire({
                            position: 'center',
                            type: 'success',
                            title: 'Quiz cadastrado com sucesso',
                            showConfirmButton: false,
                            timer: 2500
                        })
                        window.setTimeout(function(){ 
                            document.location = data.url_retorno;
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

// Metodo de editar quiz
$('.editar-quiz').click(function(e) {
    var uuid_quiz, titulo_quiz;
    uuid_quiz = $(this).attr("cs-id");
    titulo_quiz = $(this).attr("cs-titulo");

    Swal.fire({
        title: 'Editando quiz',
        input: 'text',
        inputValue: titulo_quiz,
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
                return 'Preencha o nome do quiz!'
            }
        },
        preConfirm: (value) => {
            //token de sessao
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                headers : {'X-CSRFToken': csrftoken},
                type    : 'POST',
                url     : "/quiz/editar_quiz/",
                data    : {"titulo":value, "uuid_quiz": uuid_quiz},
                datatype: 'json',

                success: function(data) {
                    if(data.status == "OK"){
                        Swal.fire({
                            position: 'center',
                            type: 'success',
                            title: 'Quiz editado com sucesso',
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