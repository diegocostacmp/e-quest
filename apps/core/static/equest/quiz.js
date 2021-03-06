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
    url_destiny = $(this).attr('eg-url');
    uuid_edit = $(this).attr('eg-uuid');

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
                        const Toast = Swal.mixin({
                            toast: true,
                            position: 'top-end',
                            showConfirmButton: false,
                            timer: 3000
                        });
                        Toast.fire({
                            type: 'success',
                            title: 'Quiz excluido com sucesso!',
                            onClose: () =>{
                                location.reload();
                            }
                        })
                    }
                },
                error: function(){
                    const Toast = Swal.mixin({
                        toast: true,
                        position: 'top-end',
                        showConfirmButton: false,
                        timer: 3000
                    });
                    Toast.fire({
                        type: 'error',
                        title: 'Existem dependências associadas!',
                        onClose: () =>{
                            location.reload();
                        }
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
                    'name': value,
                    'discipline': discipline} ,
                datatype: 'json',

                success: function(data) {
                    if(data.status == "OK"){
                        const Toast = Swal.mixin({
                            toast: true,
                            position: 'top-end',
                            showConfirmButton: false,
                            timer: 3000
                        });
                        Toast.fire({
                            type: 'success',
                            title: 'Quiz cadastrado com sucesso!',
                            onClose: () =>{
                                location.reload();
                            }
                        })
                    }
                },
                error: function(data){
                    const Toast = Swal.mixin({
                        toast: true,
                        position: 'top-end',
                        showConfirmButton: false,
                        timer: 3000
                    });
                    Toast.fire({
                        type: 'error',
                        title: 'Houve algum erro ao criar o quiz!',
                        onClose: () =>{
                            location.reload();
                        }
                    })
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
                        const Toast = Swal.mixin({
                            toast: true,
                            position: 'top-end',
                            showConfirmButton: false,
                            timer: 3000
                        });
                        Toast.fire({
                            type: 'success',
                            title: 'Quiz editado com sucesso!',
                            onClose: () =>{
                                location.reload();
                            }
                        })
                    }
                },
                error: function(data){
                    const Toast = Swal.mixin({
                        toast: true,
                        position: 'center',
                        showConfirmButton: false,
                        timer: 3000
                    });
                    Toast.fire({
                        type: 'success',
                        title: 'Tivemos algum problema ao editars!',
                        onClose: () =>{
                            location.reload();
                        }
                    })
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

// Preview question
function questionBookPreview(questionUuid){
    //variables
    var csrftoken, optA, optB, optC, optD, alternativeTrue;
    //token de sessaos
    var csrftoken = getCookie('csrftoken');
    
    $.ajax({
        headers : {'X-CSRFToken': csrftoken},
        type    : 'POST',
        url     : "/quiz/question_book_preview/",
        data    : {"questionUuid": questionUuid},
        datatype: 'json',

        success: function(context){
            // Exibe modal
            $('#question_preview_manager').modal('show');
            
            // html data
            $('#body_question_preview').html(context.string_html);
            
            // Input data variables
            $("#questionTitle").html(context.title);
            optA = $("#optA").html(context.optA);
            optB = $("#optB").html(context.optB);
            optC = $("#optC").html(context.optC);
            optD = $("#optD").html(context.optD);
            alternativeTrue = context.alternativeTrue;

            $("#question-title-preview").html("Pergunta:").css('h1');

            if(alternativeTrue ==  "A"){
                $("#trueA").addClass("fa fa-check");

            }else if(alternativeTrue == "B"){
                $("#trueB").addClass("fa fa-check");

            }else if(alternativeTrue == "C"){
                $("#trueC").addClass("fa fa-check");

            }else{
                $("#trueD").addClass("fa fa-check");

            }

        },
        error: function(){
            console.log('Houve algum problema ao abrir o modal');
        }
    });
}

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
                //token de sessao
                var  quiz_uuid, csrftoken, msg_A, msg_B, msg_C, msg_D, seconds, message, optSelected, quiz_uuid;
                quiz_uuid = $('#quiz-uuid').val();
                message = $('#message').val();
                msg_A = $('#kt_autosize_A').val();
                msg_B = $('#kt_autosize_B').val();
                msg_C = $('#kt_autosize_C').val();
                msg_D = $('#kt_autosize_D').val();
                seconds = $('#kt_autosize_seconds').val();
                optSelected = $('input[name=question_selected]:checked', '#form-alternatives').val();
                
                if(optSelected == undefined){
                    Swal.fire({
                        type: 'warning',
                        title: 'Selecione a alternativa correta!'
                    })
                }else{
                    csrftoken = getCookie('csrftoken');
                    
                    $.ajax({
                        headers : {'X-CSRFToken': csrftoken},
                        type    : 'POST',
                        url     : '/quiz/question_create/',
                        data    : {
                            'quiz_uuid':quiz_uuid,
                            'message': message,
                            'msg_A': msg_A,
                            'msg_B': msg_B,
                            'msg_C': msg_C,
                            'msg_D': msg_D,
                            'seconds': seconds,
                            'optSelected': optSelected
                        },
                        datatype: 'json',
    
                        success: function(data) {
                            if(data.status == "OK"){
                                $('#question_manager').modal('hide');
                                const Toast = Swal.mixin({
                                    toast: true,
                                    position: 'top-end',
                                    showConfirmButton: false,
                                    timer: 3000
                                });
                                Toast.fire({
                                    type: 'success',
                                    title: 'Cadastrado com sucesso!',
                                    onClose: () =>{
                                        location.reload();
                                    }
                                })
                                
                            }
                        },
                        error: function(data){
                            if(data.status == ""){
                                Swal.fire({
                                    type: 'error',
                                    title: 'Desculpe...',
                                    text: data.msg_return
                                })
    
                            }
                        }
                    })

                }
                
            }
        })      
    }
    return {
        // public functions
        init: function() {
            questionValidate(); 
        }
    };
}();

$('.question-delete').click(function(e) {
    var url_destiny, uuid_edit;
    url_destiny = $(this).attr('eg-url');
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
                        const Toast = Swal.mixin({
                            toast: true,
                            position: 'top-end',
                            showConfirmButton: false,
                            timer: 3000
                        });
                        Toast.fire({
                            type: 'success',
                            title: 'Excluído com sucesso!',
                            onClose: () =>{
                                location.reload();
                            }
                        })
                        
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

$(document).ready(function () { 
    KTAutosize.init(); 
    KTFormControls.init();
    
});