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

// As classes e acoes comuns a todos os Apps
// devem ser inseridos neste arquivo.
$('.discipline-delete').click(function(e) {
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
                            title: 'Cadastrado excluido com sucesso!',
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

// Chamada do metodo cadastrar_Discipline
$('#discipline-create').click(function(e) {
    Swal.fire({
        title: 'Digite o nome da Disciplina',
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
                return 'Preencha o nome da Disciplina!'
            }
        },
        preConfirm: (value) => {
            //token de sessao
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                headers : {'X-CSRFToken': csrftoken},
                type    : 'POST',
                url     : '/discipline_create/',
                data    : {'name':value},
                datatype: 'json',

                success: function(data) {
                    if(data.status == "OK"){
                        console.log("saida:", data.table)
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
                                // reload only table
                                $("#disciplineList").append(data.table);
                            }
                        })
                    }
                },
                error: function(data){
                    alert('deu erro');
                }
            });
        },
    })
});

// Metodo de cadastro de Discipline
$('.discipline-edit').click(function(e) {
    var discipline_uuid, discipline_title;
    discipline_uuid = $(this).attr("eg-id");
    discipline_title = $(this).attr("eg-title");

    Swal.fire({
        title: 'Editando Disciplina',
        input: 'text',
        inputValue: discipline_title,
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
                return 'Preencha o nome da Disciplina!'
            }
        },
        preConfirm: (value) => {
            //token de sessao
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                headers : {'X-CSRFToken': csrftoken},
                type    : 'POST',
                url     : "/discipline_edit/",
                data    : {"title":value, "discipline_uuid": discipline_uuid},
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
                            title: 'Editado com sucesso!',
                            onClose: () =>{
                                location.reload();
                            }
                        })
                    }
                },
                error: function(data){
                    alert('deu erro');
                }
            });
        },
    })
});




