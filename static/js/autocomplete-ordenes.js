/**
 * DIGIT SOFT - Autocompletado de Clientes y Técnicos
 * Sistema de autocompletado con jQuery UI
 */

(function($) {
    'use strict';

    // Autocompletado de Clientes
    function initClienteAutocomplete(inputSelector, hiddenIdSelector) {
        $(inputSelector).autocomplete({
            source: function(request, response) {
                $.ajax({
                    url: '/ordenes/api/clientes/',
                    data: {
                        term: request.term
                    },
                    dataType: 'json',
                    success: function(data) {
                        response(data);
                    },
                    error: function() {
                        response([]);
                    }
                });
            },
            minLength: 2,
            select: function(event, ui) {
                // Establecer el valor del campo visible
                $(this).val(ui.item.value);

                // Establecer el ID en el campo oculto
                if (hiddenIdSelector) {
                    $(hiddenIdSelector).val(ui.item.id);
                }

                // Llenar campos adicionales si existen
                if ($('#cliente_documento').length) {
                    $('#cliente_documento').val(ui.item.documento);
                }
                if ($('#cliente_telefono').length) {
                    $('#cliente_telefono').val(ui.item.telefono);
                }
                if ($('#cliente_correo').length) {
                    $('#cliente_correo').val(ui.item.correo);
                }

                return false;
            },
            focus: function(event, ui) {
                $(this).val(ui.item.value);
                return false;
            }
        }).autocomplete("instance")._renderItem = function(ul, item) {
            return $("<li>")
                .append("<div class='autocomplete-item'>" +
                        "<strong>" + item.value + "</strong><br>" +
                        "<small class='text-muted'>" + item.documento + "</small>" +
                        "</div>")
                .appendTo(ul);
        };
    }

    // Autocompletado de Técnicos
    function initTecnicoAutocomplete(inputSelector, hiddenIdSelector) {
        $(inputSelector).autocomplete({
            source: function(request, response) {
                $.ajax({
                    url: '/ordenes/api/tecnicos/',
                    data: {
                        term: request.term
                    },
                    dataType: 'json',
                    success: function(data) {
                        response(data);
                    },
                    error: function() {
                        response([]);
                    }
                });
            },
            minLength: 2,
            select: function(event, ui) {
                // Establecer el valor del campo visible
                $(this).val(ui.item.value);

                // Establecer el ID en el campo oculto
                if (hiddenIdSelector) {
                    $(hiddenIdSelector).val(ui.item.id);
                }

                // Llenar campos adicionales si existen
                if ($('#tecnico_documento').length) {
                    $('#tecnico_documento').val(ui.item.documento);
                }
                if ($('#tecnico_telefono').length) {
                    $('#tecnico_telefono').val(ui.item.telefono);
                }

                return false;
            },
            focus: function(event, ui) {
                $(this).val(ui.item.value);
                return false;
            }
        }).autocomplete("instance")._renderItem = function(ul, item) {
            return $("<li>")
                .append("<div class='autocomplete-item'>" +
                        "<strong>" + item.value + "</strong><br>" +
                        "<small class='text-muted'>" + item.label.split(' - ')[1] + "</small>" +
                        "</div>")
                .appendTo(ul);
        };
    }

    // Inicialización cuando el documento esté listo
    $(document).ready(function() {
        // Autocompletado de clientes en formularios de órdenes
        if ($('#cliente_autocomplete').length) {
            initClienteAutocomplete('#cliente_autocomplete', '#id_cliente');
        }

        // Autocompletado de técnicos en formularios de órdenes
        if ($('#tecnico_autocomplete').length) {
            initTecnicoAutocomplete('#tecnico_autocomplete', '#id_tecnico_asignado');
        }

        // Búsqueda de clientes en filtros
        if ($('#buscar_cliente').length) {
            initClienteAutocomplete('#buscar_cliente', null);
        }

        // Búsqueda de técnicos en filtros
        if ($('#buscar_tecnico').length) {
            initTecnicoAutocomplete('#buscar_tecnico', null);
        }
    });

    // Exportar funciones para uso externo
    window.DigitSoft = window.DigitSoft || {};
    window.DigitSoft.initClienteAutocomplete = initClienteAutocomplete;
    window.DigitSoft.initTecnicoAutocomplete = initTecnicoAutocomplete;

})(jQuery);

