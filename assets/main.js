(function(){
'use strict';
var hdr=document.querySelector('.site-header');
var bar=document.createElement('div');bar.className='progress';document.body.appendChild(bar);
function onScroll(){
  var y=window.scrollY;
  if(hdr)hdr.classList.toggle('scrolled',y>10);
  var h=document.documentElement.scrollHeight-innerHeight;
  bar.style.width=(h>0?y/h*100:0)+'%';
}
addEventListener('scroll',onScroll,{passive:true});onScroll();
var bg=document.querySelector('.burger');
if(bg)bg.onclick=function(){document.body.classList.toggle('menu-open')};
document.querySelectorAll('.nav .dd').forEach(function(d){
  var b=document.createElement('button');b.type='button';b.className='dd-t';b.setAttribute('aria-label','Show submenu');b.setAttribute('aria-expanded','false');
  b.innerHTML='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>';
  b.onclick=function(e){e.preventDefault();var o=d.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false')};
  d.insertBefore(b,d.children[1]);
});
document.querySelectorAll('.nav a').forEach(function(a){a.addEventListener('click',function(){document.body.classList.remove('menu-open')})});

// split headings into words
document.querySelectorAll('[data-split]').forEach(function(el){
  (function walk(node){
    Array.prototype.slice.call(node.childNodes).forEach(function(n){
      if(n.nodeType===3){
        var f=document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(function(t){
          if(!t)return;
          if(/^\s+$/.test(t)){f.appendChild(document.createTextNode(' '));return}
          var w=document.createElement('span');w.className='w';var s=document.createElement('span');s.textContent=t;w.appendChild(s);f.appendChild(w);
        });
        n.replaceWith(f);
      }else if(n.nodeType===1&&!n.classList.contains('w'))walk(n);
    });
  })(el);
  el.querySelectorAll('.w>span').forEach(function(s,i){s.style.transitionDelay=(i*0.055)+'s'});
  el.classList.add('split');
});

// stagger children
document.querySelectorAll('[data-stagger]').forEach(function(p){
  Array.prototype.slice.call(p.children).forEach(function(c,i){c.classList.add('rv');c.style.setProperty('--d',(i*0.08)+'s')});
});
document.querySelectorAll('[data-delay]').forEach(function(el){el.style.setProperty('--d',el.dataset.delay+'s')});

function count(el){
  var end=parseFloat(el.dataset.count),suf=el.dataset.suffix||'',t0=performance.now();
  (function tick(t){var p=Math.min((t-t0)/1500,1),e=1-Math.pow(1-p,3);
    el.innerHTML=Math.round(end*e)+(suf?'<i>'+suf+'</i>':'');if(p<1)requestAnimationFrame(tick)})(t0);
}
var io=new IntersectionObserver(function(es){es.forEach(function(e){
  if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);if(e.target.dataset.count!==undefined)count(e.target)}
})},{threshold:.12,rootMargin:'0px 0px -5% 0px'});
document.querySelectorAll('.rv,.split,[data-count]').forEach(function(el){io.observe(el)});
// safety: never leave content hidden
setTimeout(function(){document.querySelectorAll('.rv:not(.in),.split:not(.in)').forEach(function(el){var r=el.getBoundingClientRect();if(r.top<innerHeight*1.2)el.classList.add('in')})},2500);

document.querySelectorAll('[data-filter]').forEach(function(g){
  var btns=g.querySelectorAll('.fbtn'),items=document.querySelectorAll(g.dataset.filter+' [data-cat]');
  btns.forEach(function(b){b.addEventListener('click',function(){
    btns.forEach(function(x){x.classList.toggle('on',x===b)});
    items.forEach(function(it){var ok=b.dataset.f==='all'||it.dataset.cat.split(' ').indexOf(b.dataset.f)>-1;it.classList.toggle('hide',!ok)});
  })});
});
document.querySelectorAll('form[data-demo]').forEach(function(f){f.addEventListener('submit',function(e){
  e.preventDefault();
  var ok=f.parentNode.querySelector('.ok')||f.querySelector('.ok');
  if(f.dataset.mailto&&f.dataset.subject){
    var em=f.elements.email?f.elements.email.value:'';
    window.location.href='mailto:'+f.dataset.mailto+'?subject='+encodeURIComponent(f.dataset.subject)+'&body='+encodeURIComponent('Please add this email address to the ARRON blog and newsletter list:\n\n'+em);
  } else if(f.dataset.mailto){
    var g=function(n){var el=f.elements[n];return el?el.value:''};
    var body='Name: '+g('name')+'\nEmail: '+g('email')+'\nCompany: '+g('company')+'\nInterested in: '+g('topic')+'\n\n'+g('msg');
    window.location.href='mailto:'+f.dataset.mailto+'?subject='+encodeURIComponent('Enquiry from the ARRON website - '+g('topic'))+'&body='+encodeURIComponent(body);
  }
  if(ok)ok.style.display='block';f.reset();
})});
})();
