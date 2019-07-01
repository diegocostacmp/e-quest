// As classes e acoes comuns a todos os Apps
// devem ser inseridos neste arquivo.

$('.excluir-disciplina').click(function(e) {
    var url_destino, uuid_editando;
    url_destino = $(this).attr('cs-url');
    uuid_editando = $(this).attr('cs-id');

    console.log(url_destino);


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
                            'Your file has been deleted.',
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
                        text: 'Tivemos algum problema!'
                    })
                }
            });
        },
    })
})

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

