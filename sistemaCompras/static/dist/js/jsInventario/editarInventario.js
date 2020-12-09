$(document).ready(function () {
    $('#usersis').select2();
    //    Validando los campos a ingresar
    const $depa = $('#departamento');
    const $muni = $('#municipio');
    $depa.change(function () {
        $muni.val('');

        $muni.prop('disabled', !Boolean($depa.val()));
        $muni.find('option[data-region]').hide();
        $muni.find('option[data-region="' + $depa.val() + '"]').show();
    });
    $('[data-mask]').inputmask();
    var nombre, telefono, direccion, dep, muni, usersis
    $('#guardar').on('click', function () {

        nombre = $('#nombre').val();
        telefono = $('#telefono').val();
        direccion = $('#direccion').val();
        dep = $('#departamento').val();
        muni = $('#municipio').val();
        usersis = $('#usersis').val();
        

        if (nombre.length == 0 || nombre.trim() == "" ) {
            $(document).Toasts('create', {
                class: 'bg-danger',
                title: 'Empresa Proveedora',
                fade: true,
                delay: 4000,
                autohide: true,
                subtitle: 'Error en el registro',
                body: 'No se ha ingresado el nombre'
            });
        } else if (dep.length == 0 || dep.trim() == "" || muni.length == 0 || muni.trim() == "" || direccion.length == 0 || direccion.trim() == "") {
            $(document).Toasts('create', {
                class: 'bg-danger',
                title: 'Empresa Proveedora',
                fade: true,
                delay: 4000,
                autohide: true,
                subtitle: 'Error en el registro',
                body: 'No se ha ingresado todos los datos referentes a la direccion'
            });
        } else if (usersis.length == 0 || usersis.trim() == "") {
            $(document).Toasts('create', {
                class: 'bg-danger',
                title: 'Empresa Proveedora',
                fade: true,
                delay: 4000,
                autohide: true,
                subtitle: 'Error en el registro',
                body: 'No se ha seleccionado el usuario del empleado'
            });
        } else {
            document.formularioEditar.submit()
        }
    });
});