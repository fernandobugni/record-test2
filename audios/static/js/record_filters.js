var checkFilters = function(volumen) {

    resFail = 'La calidad del audio no es buena. Por favor grabar nuevamente.';
    resOK = 'Grabación exitosa';

    var res;
    $.when(firstLastFilter(volumen), umbralFilter(volumen)).done(function(r1, r2){
        console.debug('firstLastFilter: ' + r1);
        console.debug('umbralFilter: ' + r2);
        if (r1 == r2){
            res = resOK;
        }else{
            res = resFail;
        }
    });
    //return res;
    return resOK;
};

/////////////////////////////////////////////////////////////////////////////

var umbralFilter = function(volumen) {
    
    var maxVolumen = 0;

    for (var i = 0; i < volumen.length; i++) {
        if (volumen[i] > maxVolumen){
            maxVolumen = volumen[i];
        }
    };

    if (maxVolumen > maxVolumenLevel) {
        return 'Graba devuelta, mucha saturación'
    }

    if (minVolumenLevel > maxVolumen) {
        return 'Graba devuelta, volumen muy bajo';
    }

    return 'OK';
};

var firstLastFilter = function(volumen) {

    //rango por lo que debe estar el silencio del principio y el final
    var range = {min: 0, max: 8};
    //cantidad de elementos que debe haber de silencio al principio y al final
    var longit = 5;

    var cant = 0;

    for (var i = 0; i < (volumen.length / 2); i++) {
        
        var fstElem = (range.min <= volumen[i]) && (volumen[i] <= range.max);
        var LstElem = (range.min <= volumen[volumen.length - i - 1]) && (volumen[volumen.length - i - 1] <= range.max);

        console.debug('fstElem: vol['+i+']: '+volumen[i]+' res= '+fstElem+',,,, vol['+(volumen.length - i - 1)+']: '+(volumen[volumen.length - i - 1])+' res= '+LstElem);

        if (fstElem && LstElem) {
            //console.debug('Entramos');
            cant = cant + 1;
        } else {
            break;
        }
    };

    if (cant < longit) {
        return 'Grabar devuelta, debe haber silencio al principio y al final de la grabación';
    }

    return  'OK';
};