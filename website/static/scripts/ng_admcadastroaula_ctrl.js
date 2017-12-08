app.config(['$httpProvider', '$interpolateProvider',
    function($httpProvider, $interpolateProvider) {
    /* for compatibility with django teplate engine */
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    /* csrf */
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    //$httpProvider.defaults.withCredentials = true;
}]);

app.controller('AdmCadastroAulaCtrl', function($window, $http, $rootScope, $sce){
	this.videos = [];
	this.ipUrlVideo = "";
	//this.videos.push($sce.trustAsResourceUrl(this.ipUrlVideo));


	this.mostrarVideo = function(){

        if(this.videos.length > 0){
            this.videos.splice(0);
        }
		
		this.videos.push($sce.trustAsResourceUrl(this.ipUrlVideo));
	}
});

app.directive('myEnter', function () {
    return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.myEnter);
                });

                event.preventDefault();
            }
        });
    };
});
