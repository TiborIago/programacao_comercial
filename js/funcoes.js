function minhaFuncao1()
{
    $('#area-01').css({
        color: '#0000ff',
        textTransform: 'lowercase',
        width: '30%'
    });

};
 function minhaFuncao2()
{
    $('#area-02').empty();

    var alunos= ['Aluno 01, ', 'Aluno 02, ', 'Aluno 03, ', 'Aluno 04, ', 'Aluno 05. '] ;

   $.each(alunos, function (index, value){
        $('#area-02').append(value);
   });
};

function minhaFuncao3()
{
    $('#area-01').empty();

    var alunos = [
        {
            nome: 'Aluno 01',
            idade: 11
        },
        {
            nome: 'Aluno 02',
            idade: 22
        },
        {
            nome: 'Aluno 03',
            idade: 33
        },
        {
            nome: 'Aluno 04',
            idade: 55
        },
    ];
    for(i=0;i<5;i++)
    {
        console.log(alunos[i]);
    }

    var list = $("#area-01").append('<ul></ul>').find('ul');
    $.each(alunos, function(index, value) {
        list.append('<li>' + value.nome + ' -' + value.idade + '</li>');
    });
};