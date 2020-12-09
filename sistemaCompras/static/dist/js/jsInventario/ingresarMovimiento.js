$(document).ready(function () {
    var cantidad,tipo,costo
    $('#guardar').on('click', function () {

        cantidad = $('#cantidad').val();
        tipo = $('#tipo').val();
        costo = $('#costo_unitario').val();
        

        if (cantidad.length == 0 || cantidad.trim() == "") {
            $(document).Toasts('create', {
                class: 'bg-danger',
                title: 'Movimiento de inventario',
                fade: true,
                delay: 4000,
                autohide: true,
                subtitle: 'Error en el registro',
                body: 'No se ha ingresado el cantidad'
            });
        } else if (tipo.length == 0 || tipo.trim() == "") {
            $(document).Toasts('create', {
                class: 'bg-danger',
                title: 'Movimiento de inventario',
                fade: true,
                delay: 4000,
                autohide: true,
                subtitle: 'Error en el registro',
                body: 'No se ha ingresado el tipo'
            });
     
        }else if (costo.length == 0 || costo.trim() == "") {
            $(document).Toasts('create', {
                class: 'bg-danger',
                title: 'Movimiento de inventario',
                fade: true,
                delay: 4000,
                autohide: true,
                subtitle: 'Error en el registro',
                body: 'No se ha ingresado el costo'
            });
     
        } else {
            document.formulario.submit()
        }
    });
});