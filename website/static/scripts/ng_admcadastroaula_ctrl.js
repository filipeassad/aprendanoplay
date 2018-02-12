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

app.controller('AdmCadastroAulaCtrl', function($window, $http, $rootScope, $sce, $scope){
	
    $scope.videos = [];    
    $scope.cursos = [];
    $scope.modulos = [];
    $scope.moduloSel = null;
    $scope.selecionado = null;

    if(aulaEditar == null){

        $scope.ipUrlVideo = "";
        $scope.nome = "";
        $scope.descricao = "";
    
     }else{
        $scope.ipUrlVideo = aulaEditar.url_aula;
        $scope.nome = aulaEditar.nome;
        $scope.descricao = aulaEditar.descricao;
     }

	//this.videos.push($sce.trustAsResourceUrl(this.ipUrlVideo));

    $http({method: 'GET', url: urlServer + 'api/cursos', withCredentials: true }).
            success(function(data, status, headers, config) {
                
                console.log(data);
                if(data != "Erro02"){
                    for(i=0; i < data.length; i++){
                        data[i].cla = "item-lista";
                        if(data[i].nome.length > 40){
                            data[i].nome = data[i].nome.substring(0, 38) + "..."; 
                        }
                    }

                    $scope.cursos = data;

                    if(aulaEditar != null){

                        $scope.selecionado = aulaEditar.modulo.curso;
                        for(i=0; i < $scope.cursos.length; i++){
                            if($scope.cursos[i].id == aulaEditar.modulo.curso.id){
                                $scope.cursos[i].cla = "item-lista-selecionado";
                            }else{
                                $scope.cursos[i].cla = "item-lista";
                            }
                        }

                        $http({method: 'GET', url: urlServer + 'api/modulo', 
                                withCredentials: true, params: {id: aulaEditar.modulo.curso.id}}).
                                success(function(data, status, headers, config) {
                                    
                                    if(data != "Não encontrado"){
                                        $scope.modulos = data;
                                        if($scope.modulos.length > 0){
                                            for(i=0; i< $scope.modulos.length; i++){
                                                if($scope.modulos[i].id == aulaEditar.modulo.id){
                                                    $scope.moduloSel = $scope.modulos[i];
                                                }
                                            }
                                            
                                        }
                                    }

                                }).error(function(data, status, headers, config) {
                                    console.log("Não Funcionou");
                                      
                            });
                    }
                }

            }).error(function(data, status, headers, config) {
                console.log("Não Funcionou");                 
        });

    $scope.selecionaCurso = function(cur){

        $scope.selecionado = cur;

        for(i=0; i < $scope.cursos.length; i++){
            if($scope.cursos[i].id == cur.id){
                $scope.cursos[i].cla = "item-lista-selecionado";
            }else{
                $scope.cursos[i].cla = "item-lista";
            }
        }

        $scope.moduloSel = null;

        $http({method: 'GET', url: urlServer + 'api/modulo', 
                withCredentials: true, params: {id: cur.id}}).
                success(function(data, status, headers, config) {
                    
                    if(data != "Não encontrado"){
                        $scope.modulos = data;
                        if($scope.modulos.length > 0){
                            $scope.moduloSel = $scope.modulos[0];
                        }
                    }

                }).error(function(data, status, headers, config) {
                    console.log("Não Funcionou");
                      
            });

    }

	$scope.mostrarVideo = function(){

        if($scope.videos.length > 0){
            $scope.videos.splice(0);
        }
		
		$scope.videos.push($sce.trustAsResourceUrl($scope.ipUrlVideo));
	}

    $scope.salvar = function(){

        if($scope.selecionado == null){
            alert("É necessário selecionar um curso.");
            return;
        }

        if($scope.moduloSel == null){
            alert("É necessário selecionar um módulo.");
            return;
        }

        if($scope.nome.trim() == ""){
            alert("É necessário informar o nome.");
            return;
        }

        if($scope.descricao.trim() == ""){
            alert("É necessário informar a descrição.");
            return;
        }

        if($scope.ipUrlVideo.trim() == ""){
            alert("É necessário informar url do vídeo.");
            return;
        }

        var aula = null;

        if(aulaEditar == null){
            aula = {
                'tp_req': "inserir",
                'nome': $scope.nome,
                'descricao': $scope.descricao,
                'id_modulo': $scope.moduloSel.id,
                'url_aula' : $scope.ipUrlVideo
            }
        }else{
            aula = {
                'tp_req': "editar",
                'id': aulaEditar.id,
                'nome': $scope.nome,
                'descricao': $scope.descricao,
                'id_modulo': $scope.moduloSel.id,
                'url_aula': $scope.ipUrlVideo
            }
        }

        $http({method: 'POST', url: urlServer + 'api/aula', data: aula }).
            success(function(data, status, headers, config) {
                if(data == "sucesso"){
                    
                    $scope.selecionado = null;
                    $scope.nome = "";
                    $scope.descricao = "";
                    $scope.ipUrlVideo = "";
                    $scope.moduloSel = null;
                    $scope.modulos = [];
                    $scope.videos = [];

                    for (i=0;i < $scope.cursos.length; i++){
                        $scope.cursos[i].cla = "item-lista";
                    }

                    if(aulaEditar != null){
                        aulaEditar == null;
                    }

                    alert("Curso cadastrado com sucesso!");

                }else{
                    
                }         
            }).
            error(function(data, status, headers, config) {
                alert("Não foi possível cadastrar o curso!");                   
            }); 

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
