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

$('.quiz-delete').click(function(e) {
    var url_destiny, uuid_edit;
    url_destiny = $(this).attr('cs-url');
    uuid_edit = $(this).attr('eg-id');

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
                url     : String(url_destiny),
                data    : {'uuid_edit':uuid_edit},
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
$('#quiz-create').click(function(e) {

    // Get uuid Discipline
    var discipline = $('#discipline-uuid').val();

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
                url     : '/quiz/quiz_create/',
                data    : {
                    'nome': value,
                    'discipline': discipline} ,
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
                            document.location = data.url_return;
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
$('.quiz-edit').click(function(e) {
    var uuid_quiz, titles_quiz;
    uuid_quiz = $(this).attr("eg-id");
    title_quiz = $(this).attr("eg-title");

    Swal.fire({
        title: 'Editando quiz',
        input: 'text',
        inputValue: title_quiz,
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
                url     : "/quiz/quiz_edit/",
                data    : {"title":value, "uuid_quiz": uuid_quiz},
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

// Adding question with your awnser
 function questionBook(){
    var quiz_uuid = $('#question-create').val();

    //token de sessao
    var csrftoken = getCookie('csrftoken');
    
    $.ajax({
        headers : {'X-CSRFToken': csrftoken},
        type    : 'POST',
        url     : "/quiz/question_book/",
        data    : {"quiz_uuid":quiz_uuid},
        datatype: 'json',

        success: function(context){
            // Exibe modal
            $('#question_manager').modal('show');
            
            // html data
            $('#modal_body_question').html(context.data);
        },
        error: function(){
            console.log('Houve algum problema ao abrir o modal');
        }
    });
}
$('#question-save').click(function(){
    alert('click to save.');
});

var KTAutosize = { 
    init: function () {
        var i; 
        i = $("#kt_autosize"), autosize(i), autosize.update(i) 
    } 
};

// Class definition
var KTFormControls = function () {
    // Private functions
    
    var questionValidate = function () {
        $( "#question_form").validate({
            // define validation rules
            rules: {
                message: {
                    required: true,
                    minlength: 10,
                    maxlength: 1024,
                },
                kt_autosize_A:{
                    required: true
                },
                kt_autosize_B:{
                    required: true
                },
                kt_autosize_C:{
                    required: true
                },
                kt_autosize_D:{
                    required: true
                },
                kt_autosize_seconds:{
                    required: true
                }
            },
            
            //display error alert on form submit  
            invalidHandler: function(event, validator) {     
                var alert = $('#message');
                alert.removeClass('kt--hide').show();
                KTUtil.scrollTop();
            },
            submitHandler: function (form) {
                //form[0].submit(); // submit the form
            }
        });       
    }
    return {
        // public functions
        init: function() {
            questionValidate(); 
        }
    };
}();

$(document).ready(function () { 
    KTAutosize.init(); 
    KTFormControls.init();
    
});