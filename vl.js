/*
 * Audience measurement (Umami, self-hosted, cookieless).
 * Host and website ID live here only: switching to stats.lauriat.fr later
 * means editing HOST below, nothing else.
 */
(function () {
  var HOST = 'https://raspcorse.sable-qilin.ts.net:8443';
  var ID = '5f0bf16b-8571-46a5-ae7c-15e353a40527';
  var DOMAINS = 'vincentlauriat.github.io';

  var s = document.createElement('script');
  s.defer = true;
  s.src = HOST + '/insights.js';
  s.setAttribute('data-website-id', ID);
  s.setAttribute('data-host-url', HOST);
  s.setAttribute('data-domains', DOMAINS);
  document.head.appendChild(s);

  // Outbound links: GitHub tracked separately, everything else as clic_sortant.
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="http"]');
    if (!a || a.hostname === location.hostname || !window.umami) return;
    var name = a.hostname.indexOf('github.com') > -1 ? 'clic_github' : 'clic_sortant';
    window.umami.track(name, { url: a.href });
  }, true);
})();
