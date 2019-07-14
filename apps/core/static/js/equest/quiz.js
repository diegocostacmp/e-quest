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