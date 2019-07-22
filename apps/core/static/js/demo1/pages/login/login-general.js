
"use strict";

// Class Definition
var KTLoginGeneral = function() {

    var login = $('#kt_login');

    var showErrorMsg = function(form, type, msg) {
        var alert = $('<div class="kt-alert kt-alert--outline alert alert-' + type + ' alert-dismissible" role="alert">\
			<button type="button" class="close" data-dismiss="alert" aria-label="Close"></button>\
			<span></span>\
		</div>');

        form.find('.alert').remove();
        alert.prependTo(form);
        //alert.animateClass('fadeIn animated');
        KTUtil.animateClass(alert[0], 'fadeIn animated');
        alert.find('span').html(msg);
    }

    // Private Functions
    var displaySignUpForm = function() {
        login.removeClass('kt-login--forgot');
        login.removeClass('kt-login--signin');

        login.addClass('kt-login--signup');
        KTUtil.animateClass(login.find('.kt-login__signup')[0], 'flipInX animated');
    }

    var displaySignInForm = function() {
        login.removeClass('kt-login--forgot');
        login.removeClass('kt-login--signup');

        login.addClass('kt-login--signin');
        KTUtil.animateClass(login.find('.kt-login__signin')[0], 'flipInX animated');
        //login.find('.kt-login__signin').animateClass('flipInX animated');
    }

    var displayForgotForm = function() {
        login.removeClass('kt-login--signin');
        login.removeClass('kt-login--signup');

        login.addClass('kt-login--forgot');
        //login.find('.kt-login--forgot').animateClass('flipInX animated');
        KTUtil.animateClass(login.find('.kt-login__forgot')[0], 'flipInX animated');

    }

    var handleFormSwitch = function() {
        $('#kt_login_forgot').click(function(e) {
            e.preventDefault();
            displayForgotForm();
        });

        $('#kt_login_forgot_cancel').click(function(e) {
            e.preventDefault();
            displaySignInForm();
        });

        $('#kt_login_signup').click(function(e) {
            e.preventDefault();
            displaySignUpForm();
        });

        $('#kt_login_signup_cancel').click(function(e) {
            e.preventDefault();
            displaySignInForm();
        });
    }

    var handleSignInFormSubmit = function() {
        $('#kt_login_signin_submit').click(function(e) {
            e.preventDefault();
            var btn = $(this);
            var form = $(this).closest('form');           

            form.validate({
                rules: {
                    email: {
                        required: true,
                        email: true
                    },
                    password: {
                        required: true
                    }
                }
            });

            if (!form.valid()) {
                return;
            }

            btn.addClass('kt-spinner kt-spinner--right kt-spinner--sm kt-spinner--light').attr('disabled', true);

            // Token de sessao
            var csrftoken = getCookie('csrftoken');

            // Email e senha
            var email   = $('#email').val();
            var senha   = $('#senha').val();

            $.ajax({
                headers : {'X-CSRFToken': csrftoken},
                type    : 'POST',
                url     : '/postsign/',
                data    : {'email':email, 'senha':senha},
                datatype: 'json',

                success: function(data) {
                	if(data.status == 1){
                        document.location = data.url_retorno;
                    }
                },
                error: function(){
                    // similate 2s delay
                	setTimeout(function() {
	                    btn.removeClass('kt-spinner kt-spinner--right kt-spinner--sm kt-spinner--light').attr('disabled', false);
	                    showErrorMsg(form, 'danger', 'Email ou senha incorreto. Tente novamente.');
                    }, 2000);
                }
            });
        });
    }

    var handleSignUpFormSubmit = function() {
        $('#kt_login_signup_submit').click(function(e) {
            e.preventDefault();

            var btn = $(this);
            var form = $(this).closest('form');

            form.validate({
                rules: {
                    fullname: {
                        required: true
                    },
                    email: {
                        required: true,
                        email: true
                    },
                    password: {
                        required: true
                    },
                    // rpassword: {
                    //     required: true
                    // },
                    agree: {
                        required: true
                    }
                }
            });

            if (!form.valid()) {
                return;
            }

            btn.addClass('kt-spinner kt-spinner--right kt-spinner--sm kt-spinner--light').attr('disabled', true);

            // Obtendo dados do formulario
            var nome    = $('#nome-cadastro').val();
            var email   = $('#email-cadastro').val();
            var senha   = $('#senha-cadastro').val();
            var tipo    = $('input[name=tipo]:checked', '#cadastro-User').val(); 

            //token de sessao
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                headers : {'X-CSRFToken': csrftoken},
                type    : 'POST',
                url     : '/signup/',
                data    : {'nome':nome, 'email':email, 'senha':senha, 'tipo':tipo},
                datatype: 'json',
                success: function(response, status, xhr, $form) {
                	// similate 2s delay
                	setTimeout(function() {
	                    btn.removeClass('kt-spinner kt-spinner--right kt-spinner--sm kt-spinner--light').attr('disabled', false);
	                    form.clearForm();
	                    form.validate().resetForm();

	                    // display signup form
	                    displaySignInForm();
	                    var signInForm = login.find('.kt-login__signin form');
	                    signInForm.clearForm();
	                    signInForm.validate().resetForm();

	                    showErrorMsg(signInForm, 'success', 'Parabéns! Seu cadastro foi realizado com sucesso. Acesse e divirta-se aprendendo.');
	                }, 2000);
                },
                error: function(){
                    // similate 2s delay
                	setTimeout(function() {
	                    btn.removeClass('kt-spinner kt-spinner--right kt-spinner--sm kt-spinner--light').attr('disabled', false);
	                    showErrorMsg(form, 'danger', 'Ops! Tivemos algum problema, tente novamente.');
                    }, 2000);

                }
            });
        });
    }
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
    

    var handleForgotFormSubmit = function() {
        $('#kt_login_forgot_submit').click(function(e) {
            e.preventDefault();

            var btn = $(this);
            var form = $(this).closest('form');

            form.validate({
                rules: {
                    email: {
                        required: true,
                        email: true
                    }
                }
            });

            if (!form.valid()) {
                return;
            }

            btn.addClass('kt-spinner kt-spinner--right kt-spinner--sm kt-spinner--light').attr('disabled', true);

            form.ajaxSubmit({
                url: '',
                success: function(response, status, xhr, $form) { 
                	// similate 2s delay
                	setTimeout(function() {
                		btn.removeClass('kt-spinner kt-spinner--right kt-spinner--sm kt-spinner--light').attr('disabled', false); // remove
	                    form.clearForm(); // clear form
	                    form.validate().resetForm(); // reset validation states

	                    // display signup form
	                    displaySignInForm();
	                    var signInForm = login.find('.kt-login__signin form');
	                    signInForm.clearForm();
	                    signInForm.validate().resetForm();

	                    showErrorMsg(signInForm, 'success', 'Cool! Password recovery instruction has been sent to your email.');
                	}, 2000);
                }
            });
        });
    }

    // Public Functions
    return {
        // public functions
        init: function() {
            handleFormSwitch();
            handleSignInFormSubmit();
            handleSignUpFormSubmit();
            handleForgotFormSubmit();
        }
    };
}();

// Class Initialization
jQuery(document).ready(function() {
    KTLoginGeneral.init();
});