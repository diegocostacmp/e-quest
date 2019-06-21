$('#adicionar-disciplina').click(function(e) {
    const inputValue = ''
    
    Swal.fire({
        title: 'Informe o nome da disciplina',
        input: 'text',
        inputValue: inputValue,
        showCancelButton: true,
        inputValidator: (value) => {
            if (!value) {
                return 'Escreva o nome da disciplina!'
            }
        }
    })
});