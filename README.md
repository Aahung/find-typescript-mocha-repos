# Find Repos in TypeScript Tested using Mocha

The list was updated at 00:39:21 11/25/17 PST

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 39196 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 9374 | `cross-env TS_NODE_FAST=true mocha --compilers ts:ts-node/register --opts spec/support/coverage.opts "spec/**/*-spec.ts"` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 3837 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 2597 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 2507 | `nyc --require ts-node/register mocha src/**/*.spec.ts --reporter spec` | 
| [Microsoft/sqlopsstudio](https://github.com/Microsoft/sqlopsstudio) | 2266 | `mocha` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2188 | `mocha 'test/**/*.ts'` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1702 | `mocha` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1424 | `rimraf dist && tsc && cp -r test/fixtures dist/test && mocha dist/test --recursive` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 1389 | `mocha` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1314 | `npm run lint && npm run mocha && npm run doctest` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1221 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 1210 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1205 | `rimraf .test && mocha --timeout 30000 dist/__test__` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 1008 | `cross-env TS_NODE_PROJECT=test/tsconfig.json TS_NODE_DISABLE_WARNINGS=1 nyc mocha --opts test/mocha.opts` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 894 | `mocha --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 810 | `mocha --opts test/mocha.opts` | 
| [cherow/cherow](https://github.com/cherow/cherow) | 786 | `mocha test/specs/**/*.ts -R spec --bail` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 766 | `nyc -c -x '' mocha ./out/test --recursive` | 
| [gamestdio/colyseus](https://github.com/gamestdio/colyseus) | 713 | `mocha --require ts-node/register test/**Test.ts` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 683 | `mocha --compilers ts:ts-node/register -R spec src/**/*.spec.ts` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 629 | `npm run prettify && mocha --require ts-node/register test/**.ts test/**/*.ts` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 523 | `mocha --recursive` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 515 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 511 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 471 | `mocha --compilers ts:ts-node/register test/*.js || true` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 466 | `mocha --opts test/mocha.opts dist/test` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 445 | `mocha` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 438 | `mocha bin/tests/test.js` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 388 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [gcanti/fp-ts](https://github.com/gcanti/fp-ts) | 377 | `npm run lint && npm run prettier && npm run mocha` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 353 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 345 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 344 | `node packages/build/bin/run-nyc npm run mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 336 | `mocha` | 
| [Microsoft/BotFramework-WebChat](https://github.com/Microsoft/BotFramework-WebChat) | 335 | `concurrently  "node test/mock_dl/index.js" "mocha test" ` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 329 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 321 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 320 | `mocha --opts mocha.opts` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 315 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 305 | `yarn run lint && yarn run test:mocha` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 305 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 295 | `mocha --timeout 15000 --compilers js:babel-register ./test/*Spec.js` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 282 | `mocha` | 
| [gcanti/io-ts](https://github.com/gcanti/io-ts) | 260 | `npm run prettier && npm run lint && npm run typings-checker && npm run mocha` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 247 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 244 | `mocha --opts mocha.opts` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 242 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 238 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 228 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 227 | `mocha` | 
| [Polymer/prpl-server-node](https://github.com/Polymer/prpl-server-node) | 223 | `npm run build && mocha` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 216 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 mocha -r ts-node/register test/*.spec.ts` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 203 | `mocha -R spec test/integration` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 198 | `nyc --reporter html mocha` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 195 | `mocha dist/test/helper dist/test/unit/**` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 194 | `cross-env NODE_ENV=test mocha **/*.spec.ts --compilers ts:ts-node/register` | 
| [ethanresnick/json-api](https://github.com/ethanresnick/json-api) | 191 | `export NODE_ENV=testing; mocha --compilers ts:ts-node/register --recursive test/unit/ test/integration/` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 188 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 187 | `mocha lib/test` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 183 | `tsc && mocha --require source-map-support/register dist/test && node example/main.js ` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 182 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 182 | `mocha test` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 176 | `mocha -r ts-node/register test/**.test.ts` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 171 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 169 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [anandanand84/technicalindicators](https://github.com/anandanand84/technicalindicators) | 165 | `mocha --compilers js:babel-register --require babel-polyfill` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 163 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 163 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 163 | `npm run lint && npm run mocha` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 160 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 160 | `mocha .tmp/spec/index.spec.js` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 160 | `npm run clean && npm run build && npm run lint && mocha` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 156 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 156 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 155 | `mocha dist/test.js` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 154 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 146 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [hayjs/hay](https://github.com/hayjs/hay) | 135 | `yarn run lint && TS_NODE_PROJECT=tsconfig.test.json mocha --compilers ts:ts-node/register` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 135 | `mocha js` | 
| [PolymerLabs/polylint](https://github.com/PolymerLabs/polylint) | 133 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 133 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [Tyriar/node-pty](https://github.com/Tyriar/node-pty) | 131 | `cross-env NODE_ENV=test mocha -R spec lib/*.test.js` | 
| [Romakita/ts-express-decorators](https://github.com/Romakita/ts-express-decorators) | 121 | `npm run clean && npm run tsc && npm run tslint && NODE_ENV=test nyc --reporter=html --reporter=text _mocha --recursive` | 
| [calidion/vig](https://github.com/calidion/vig) | 115 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 114 | `mocha --timeout 10000 -u tdd ./out/tests/` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 114 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 110 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 110 | `mocha test/unit/ --exit` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 108 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 106 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [stipsan/scroll-into-view-if-needed](https://github.com/stipsan/scroll-into-view-if-needed) | 105 | `cypress run --browser chrome --reporter junit --reporter-options 'mochaFile=junit/test-results.xml'` | 
| [webshell/materia-server](https://github.com/webshell/materia-server) | 104 | `mocha -R spec dist/test/**/*.js` | 
| [frptools/collectable](https://github.com/frptools/collectable) | 102 | `mocha --opts ./mocha.opts` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 101 | `mocha` | 
| [staltz/easy-ssb-pub](https://github.com/staltz/easy-ssb-pub) | 100 | `npm run lint && npm run mocha` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 96 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 