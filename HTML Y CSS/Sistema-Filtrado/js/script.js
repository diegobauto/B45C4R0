// Activador de jQuery - Función principal de jQuery
$(document).ready(function(){

    // Funciones de Filtrado
    $('#productos').click(function(){
        $('main section#sistema-filtrado article img').show();

        $('#productos').addClass('filtro-activo');
        $('#productos').removeClass('filtro-inactivo');

        $('#camaras, #teclados, #parlantes').removeClass('filtro-activo');
        $('#camaras, #teclados, #parlantes').addClass('filtro-inactivo');
    });

    $('#camaras').click(function(){
        $('main section#sistema-filtrado article img').hide();
        $('main section#sistema-filtrado article img.camaras').show();

        $('#camaras').addClass('filtro-activo');
        $('#camaras').removeClass('filtro-inactivo');

        $('#productos, #teclados, #parlantes').removeClass('filtro-activo');
        $('#productos, #teclados, #parlantes').addClass('filtro-inactivo');
    });

    $('#teclados').click(function(){
        $('main section#sistema-filtrado article img').hide();
        $('main section#sistema-filtrado article img.teclados').show();

        $('#teclados').addClass('filtro-activo');
        $('#teclados').removeClass('filtro-inactivo');

        $('#productos, #parlantes, #camaras').removeClass('filtro-activo');
        $('#productos, #parlantes, #camaras').addClass('filtro-inactivo');
    });

    $('#parlantes').click(function(){
        $('main section#sistema-filtrado article img').hide();
        $('main section#sistema-filtrado article img.parlantes').show();

        $('#parlantes').addClass('filtro-activo');
        $('#parlantes').removeClass('filtro-inactivo');

        $('#productos, #teclados, #camaras').removeClass('filtro-activo');
        $('#productos, #teclados, #camaras').addClass('filtro-inactivo');
    });

    // Función de Posición fija de Filtros al hacer ScrollDown
    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('main section#sistema-filtrado nav#filtros').css('position','fixed');
            $('main section#sistema-filtrado nav#filtros').css('left','0');
            $('main section#sistema-filtrado nav#filtros').css('z-index','999');
            $('main section#sistema-filtrado nav#filtros').css('top','80px');
            $('main section#sistema-filtrado nav#filtros').css('border-radius','0 0 5px 5px');
        } else {
            $('main section#sistema-filtrado nav#filtros').css('position','relative');
            $('main section#sistema-filtrado nav#filtros').css('left','0');
            $('main section#sistema-filtrado nav#filtros').css('z-index','1');
            $('main section#sistema-filtrado nav#filtros').css('top','0');
            $('main section#sistema-filtrado nav#filtros').css('border-radius','5px');
        }
    });
});