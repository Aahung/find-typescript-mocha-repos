# Find Repos in TypeScript Tested using Mocha

The list was updated at 00:39:25 11/12/17 PST

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 38054 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 9157 | `cross-env TS_NODE_FAST=true mocha --compilers ts:ts-node/register --opts spec/support/coverage.opts "spec/**/*-spec.ts"` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 3737 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 2558 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 2298 | `nyc --require ts-node/register mocha src/**/*.spec.ts --reporter spec` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2180 | `mocha 'test/**/*.ts'` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1674 | `mocha` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1395 | `rimraf dist && tsc && cp -r test/fixtures dist/test && mocha dist/test --recursive` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1305 | `npm run lint && npm run mocha && npm run doctest` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 1299 | `mocha` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1220 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1189 | `rimraf .test && mocha --timeout 30000 dist/__test__` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 1161 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 955 | `cross-env TS_NODE_PROJECT=test/tsconfig.json TS_NODE_DISABLE_WARNINGS=1 nyc mocha --opts test/mocha.opts` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 865 | `mocha --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 806 | `mocha --opts test/mocha.opts` | 
| [cherow/cherow](https://github.com/cherow/cherow) | 781 | `mocha test/specs/**/*.ts -R spec --bail` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 736 | `nyc -c -x '' mocha ./out/test --recursive` | 
| [gamestdio/colyseus](https://github.com/gamestdio/colyseus) | 696 | `mocha --require ts-node/register test/**Test.ts` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 681 | `mocha --compilers ts:ts-node/register -R spec src/**/*.spec.ts` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 516 | `mocha --require ts-node/register test/**.ts test/**/*.ts` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 510 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 482 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 461 | `mocha --opts test/mocha.opts dist/test` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 460 | `mocha --compilers ts:ts-node/register test/*.js || true` | 
| [bleenco/ngx-uploader](https://github.com/bleenco/ngx-uploader) | 459 | `mocha -r ts-node/register -r ignore-styles src/**/*.spec.ts` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 437 | `mocha` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 425 | `mocha bin/tests/test.js` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 388 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 350 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [gcanti/fp-ts](https://github.com/gcanti/fp-ts) | 349 | `npm run lint && npm run prettier && npm run mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 336 | `mocha` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 332 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 330 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [Microsoft/BotFramework-WebChat](https://github.com/Microsoft/BotFramework-WebChat) | 322 | `concurrently  "node test/mock_dl/index.js" "mocha test" ` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 317 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 314 | `node packages/build/bin/run-nyc npm run mocha` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 313 | `mocha --opts mocha.opts` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 309 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 301 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 281 | `mocha` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 275 | `yarn run lint && yarn run test:mocha` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 273 | `mocha --timeout 15000 --compilers js:babel-register ./test/*Spec.js` | 
| [gcanti/io-ts](https://github.com/gcanti/io-ts) | 240 | `npm run prettier && npm run lint && npm run typings-checker && npm run mocha` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 240 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 239 | `mocha --opts mocha.opts` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 237 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 233 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 222 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 219 | `mocha` | 
| [Polymer/prpl-server-node](https://github.com/Polymer/prpl-server-node) | 217 | `npm run build && mocha` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 211 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 mocha -r ts-node/register test/*.spec.ts` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 202 | `mocha -R spec test/integration` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 196 | `nyc --reporter html mocha` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 190 | `mocha dist/test/helper dist/test/unit/**` | 
| [ethanresnick/json-api](https://github.com/ethanresnick/json-api) | 188 | `export NODE_ENV=testing; mocha --compilers ts:ts-node/register --recursive test/unit/**/*.ts test/integration/**/**/*.ts` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 188 | `cross-env NODE_ENV=test mocha **/*.spec.ts --compilers ts:ts-node/register` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 184 | `mocha lib/test` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 181 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 180 | `tsc && mocha --require source-map-support/register dist/test && node example/main.js ` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 179 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 179 | `mocha test` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 170 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 169 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 163 | `npm run lint && npm run mocha` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 162 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 158 | `npm run clean && npm run build && npm run lint && mocha` | 
| [anandanand84/technicalindicators](https://github.com/anandanand84/technicalindicators) | 157 | `mocha --compilers js:babel-register --require babel-polyfill` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 157 | `mocha dist/test.js` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 156 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 154 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 153 | `mocha .tmp/spec/index.spec.js` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 152 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 149 | `mocha -r ts-node/register test/**.test.ts` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 141 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 141 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 140 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [hayjs/hay](https://github.com/hayjs/hay) | 135 | `yarn run lint && TS_NODE_PROJECT=tsconfig.test.json mocha --compilers ts:ts-node/register` | 
| [PolymerLabs/polylint](https://github.com/PolymerLabs/polylint) | 133 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [Tyriar/node-pty](https://github.com/Tyriar/node-pty) | 130 | `cross-env NODE_ENV=test mocha -R spec lib/*.test.js` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 127 | `mocha js` | 
| [Romakita/ts-express-decorators](https://github.com/Romakita/ts-express-decorators) | 121 | `npm run clean && npm run tsc && npm run tslint && NODE_ENV=test nyc --reporter=html --reporter=text _mocha --recursive` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 119 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [calidion/vig](https://github.com/calidion/vig) | 114 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 114 | `mocha --timeout 10000 -u tdd ./out/tests/` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 113 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 110 | `mocha test/unit/ --exit` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 107 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 107 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [webshell/materia-server](https://github.com/webshell/materia-server) | 105 | `mocha -R spec dist/test/**/*.js` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 103 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 101 | `mocha` | 
| [staltz/easy-ssb-pub](https://github.com/staltz/easy-ssb-pub) | 97 | `npm run lint && npm run mocha` | 
| [stipsan/scroll-into-view-if-needed](https://github.com/stipsan/scroll-into-view-if-needed) | 97 | `cypress run --browser chrome --reporter junit --reporter-options 'mochaFile=junit/test-results.xml'` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 93 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 92 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [pana-cc/mocha-typescript](https://github.com/pana-cc/mocha-typescript) | 91 | `mocha test.js --opts mocha.opts` | 