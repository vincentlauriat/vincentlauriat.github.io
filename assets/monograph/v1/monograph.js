/* monograph.js — v1 — bascule EN / FR / 中文 commune aux fiches.
   La préférence est partagée avec le hub (même clé, même origine) : un
   visiteur qui lit le livre en français ouvre chaque fiche en français. */
(function(){
  /* zh-Hant et non zh : un simple `zh` laisse le navigateur choisir une
     fonte Han simplifiée sur un système configuré en chinois simplifié. */
  var TAG={en:'en',fr:'fr',zh:'zh-Hant'};
  function setLang(l){
    if(!TAG[l]) l='en';
    var b=document.body;
    b.classList.remove('lang-en','lang-fr','lang-zh');
    b.classList.add('lang-'+l);
    document.documentElement.lang=TAG[l];
    document.querySelectorAll('.langs button').forEach(function(x){
      var on=x.dataset.lang===l;
      x.classList.toggle('on',on);
      x.setAttribute('aria-pressed',on?'true':'false');
    });
    try{localStorage.setItem('vl-lang',l)}catch(e){}
  }
  window.setLang=setLang;
  function init(){
    var saved;try{saved=localStorage.getItem('vl-lang')}catch(e){}
    var only=document.body.dataset.langs;           /* page monolingue : data-langs="en" */
    var n=(navigator.language||'en').slice(0,2).toLowerCase();
    var l=saved||(n==='zh'?'zh':(n==='fr'?'fr':'en'));
    if(only&&only.split(' ').indexOf(l)<0) l=only.split(' ')[0];
    setLang(l);
    document.querySelectorAll('.langs button').forEach(function(x){
      x.addEventListener('click',function(){setLang(x.dataset.lang)});
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',init); else init();
})();
