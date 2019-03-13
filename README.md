# Find Repos in TypeScript Tested using Mocha

The list was updated at 01:56:15 03/13/19 PDT

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 71132 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 17413 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 13342 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 11651 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 7268 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 6646 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 5805 | `npm run mocha` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 5035 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4839 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4787 | `mocha` | 
| [rrweb-io/rrweb](https://github.com/rrweb-io/rrweb) | 4216 | `npm run bundle:browser && cross-env TS_NODE_CACHE=false TS_NODE_FILES=true mocha -r ts-node/register test/**/*.test.ts` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3444 | `mocha --opts mocha.opts` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 3317 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 3078 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [retejs/rete](https://github.com/retejs/rete) | 2951 | `BABEL_ENV=test mocha -r ts-node/register test/**.ts` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2930 | `mocha` | 
| [electron-userland/electron-forge](https://github.com/electron-userland/electron-forge) | 2691 | `cross-env TS_NODE_FILES=true yarn run mocha './tools/test-globber.ts'` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2464 | `mocha 'test/**/*.ts'` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2358 | `mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [benjamn/recast](https://github.com/benjamn/recast) | 2278 | `npm run tsc && npm run mocha` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1798 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [colyseus/colyseus](https://github.com/colyseus/colyseus) | 1585 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 1547 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1505 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [shanalikhan/code-settings-sync](https://github.com/shanalikhan/code-settings-sync) | 1501 | `npm run tslint-check && tsc -p ./ && mocha --recursive "./out/test/**/*.js"` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1495 | `nyc -x '' mocha` | 
| [cherow/cherow](https://github.com/cherow/cherow) | 1417 | `cross-env TS_NODE_PROJECT="test/tsconfig.json" mocha "test/**/*.ts" -c -R progress -r ts-node/register -r source-map-support/register --recursive --globals expect` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1368 | `mocha --opts mocha.opts` | 
| [google/clasp](https://github.com/google/clasp) | 1354 | `nyc --cache false mocha --timeout 100000 -- 'tests/**/*.js'` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1270 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1270 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [funkia/list](https://github.com/funkia/list) | 1261 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1228 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1180 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1129 | `nyc --reporter=html --reporter=text mocha` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 1119 | `tsc -p ./ && mocha` | 
| [itchio/itch](https://github.com/itchio/itch) | 1035 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [youzan/zan-proxy](https://github.com/youzan/zan-proxy) | 993 | `nyc mocha dist/**/*.spec.js` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 983 | `mocha bin/tests/test.js` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 979 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 958 | `mocha --opts test/mocha.opts` | 
| [stryker-mutator/stryker](https://github.com/stryker-mutator/stryker) | 891 | `npm run mocha` | 
| [NativeScript/nativescript-cli](https://github.com/NativeScript/nativescript-cli) | 811 | `istanbul cover ./node_modules/mocha/bin/_mocha` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 808 | `mocha --require ts-node/register` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 796 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [netgusto/nodebook](https://github.com/netgusto/nodebook) | 785 | `mocha test/backend` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 743 | `yarn run lint && yarn run test:mocha` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 740 | `mocha` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 736 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 733 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 717 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 703 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 673 | `mocha test/unit` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 663 | `mocha "out/**/*.spec.js" -s 0` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 647 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 646 | `mocha --recursive` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 629 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [googleapis/google-auth-library-nodejs](https://github.com/googleapis/google-auth-library-nodejs) | 614 | `nyc mocha build/test` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 614 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [szokodiakos/typegoose](https://github.com/szokodiakos/typegoose) | 614 | `npm run lint && nyc npm run mocha` | 
| [dsherret/ts-morph](https://github.com/dsherret/ts-morph) | 611 | `cross-env TS_NODE_COMPILER="ttypescript" TS_NODE_TRANSPILE_ONLY="true" mocha --opts mocha.opts --grep @performance --invert` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 607 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 606 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 598 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [JustClear/blurify](https://github.com/JustClear/blurify) | 597 | `mocha test/index.js` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 594 | `npm run lint && npm run mocha` | 
| [bbc/sqs-consumer](https://github.com/bbc/sqs-consumer) | 594 | `mocha` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 588 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [mateogianolio/vectorious](https://github.com/mateogianolio/vectorious) | 586 | `nyc mocha -r ts-node/register ./src/*.spec.ts` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 566 | `mocha` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 561 | `mocha test` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 553 | `tsc && mocha test && yarn lint` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 537 | `mocha --opts test/mocha.opts dist/test` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 531 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 530 | `cross-env NODE_ENV=tsoa_test mocha **/*.spec.ts --exit --compilers ts:ts-node/register` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 527 | `cd test && mocha -r ts-node/register *.ts` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 512 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [benjamn/ast-types](https://github.com/benjamn/ast-types) | 510 | `npm run gen && npm run build && npm run mocha` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 507 | `mocha --opts mocha.opts` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 503 | `npm run mocha` | 
| [Cookie-AutoDelete/Cookie-AutoDelete](https://github.com/Cookie-AutoDelete/Cookie-AutoDelete) | 500 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec ./test/*` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 498 | `npm run lint && npm run mocha` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 493 | `mocha --opts mocha.opts` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 487 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 461 | `npm run build && mocha` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 453 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 445 | `_mocha --` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 443 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 427 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 339 | `mocha` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 330 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 328 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 325 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 315 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec --bail` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 302 | `mocha lib/test` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 351 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 350 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 349 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 339 | `mocha` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 330 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 328 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 325 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 315 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec --bail` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 302 | `mocha lib/test` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 297 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [nefe/pont](https://github.com/nefe/pont) | 296 | `mocha --timeout 15000 -r ts-node/register test/**/test.ts` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 293 | `mocha` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 291 | `cd test && mocha -r ts-node/register *.ts` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 288 | `mocha-webpack "src/**/*.ts"` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 282 | `mocha` | 
| [nwtgck/piping-server](https://github.com/nwtgck/piping-server) | 282 | `mocha --require ts-node/register --timeout 10000 test/**/*.ts` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 280 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 279 | `mocha --compilers js:babel-register test/**/*.js` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 277 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 271 | `mocha src/**/*.spec.ts` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 269 | `mocha "test/**/*.spec.ts"` | 
| [slothking-online/diagram](https://github.com/slothking-online/diagram) | 269 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [juanfranblanco/vscode-solidity](https://github.com/juanfranblanco/vscode-solidity) | 268 | `nyc --require ts-node/register --require source-map-support/register mocha test/**/*.spec.ts` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 268 | `tsc && mocha dist/**/*.spec.js` | 
| [kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | 260 | `nyc mocha` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 259 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [AmirTugi/tea-school](https://github.com/AmirTugi/tea-school) | 255 | `npx ts-mocha ./src/tests/**.ts` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 252 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 252 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [googleapis/nodejs-storage](https://github.com/googleapis/nodejs-storage) | 248 | `nyc mocha build/test` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 246 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 244 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 241 | `tsc && mocha` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 235 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [Odi-ts/odi](https://github.com/Odi-ts/odi) | 235 | `nyc mocha test/**/*.test.ts --exit` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 227 | `nyc --reporter html mocha` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 227 | `cross-env NODE_ENV=test mocha --exit` | 
| [harttle/liquidjs](https://github.com/harttle/liquidjs) | 224 | `npm run build && mocha "test/**/*.ts"` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 220 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 220 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 219 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 215 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 209 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 209 | `mocha test` | 
| [Zarel/Pokemon-Showdown-Client](https://github.com/Zarel/Pokemon-Showdown-Client) | 207 | `eslint --config=.eslintrc.js --cache --cache-file=eslint-cache/base js/ data/ && eslint --config=build-tools/.eslintrc.js --cache --cache-file=eslint-cache/build build-tools/update build-tools/build-indexes && tslint --project . && tsc && node build && mocha` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 206 | `mocha dist/test.js` | 
| [R-js/blasjs](https://github.com/R-js/blasjs) | 203 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 202 | `mocha lib/spec/core` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 200 | `mocha -R spec test/integration` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 197 | `nyc mocha --recursive test/**/*.ts` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 196 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 195 | `mocha js` | 
| [emmanueltouzery/prelude-ts](https://github.com/emmanueltouzery/prelude-ts) | 192 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 191 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 186 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 183 | `npm run build && npm run mocha` | 
| [aykutkardas/Json-Function](https://github.com/aykutkardas/Json-Function) | 182 | `cross-env TS_NODE_COMPILER_OPTIONS='{ "module": "commonjs" }' mocha -r ts-node/register -r ignore-styles -r jsdom-global/register test/**/*.spec.ts` | 
| [nodejs/llhttp](https://github.com/nodejs/llhttp) | 176 | `npm run mocha && npm run lint` | 
| [PeterDing/chord](https://github.com/PeterDing/chord) | 176 | `mocha --delay` | 
| [woutervh-/typescript-is](https://github.com/woutervh-/typescript-is) | 175 | `npm run lint && npm run build && ttsc --project tsconfig-test.json && mocha` | 
| [Chinachu/Mirakurun](https://github.com/Chinachu/Mirakurun) | 175 | `mocha --exit test/*.spec.js` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 175 | `tsc && cd dist && mocha` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 174 | `tsc && mocha` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 174 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 172 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 172 | `npm run lint && npm run mocha` | 
| [Microsoft/typescript-tslint-plugin](https://github.com/Microsoft/typescript-tslint-plugin) | 170 | `mocha ./out/**/*.test.js --slow 2000 --timeout 10000` | 
| [googleapis/nodejs-translate](https://github.com/googleapis/nodejs-translate) | 169 | `nyc mocha build/test` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 167 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 166 | `nyc --reporter=html --reporter=text mocha` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 164 | `npm run clean && npm run build && npm run lint && mocha` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 163 | `gulp compile && mocha --timeout 10000 -u tdd ./out/tests/` | 
| [p-society/typeracer-cli](https://github.com/p-society/typeracer-cli) | 161 | `mocha --no-deprecation --timeout 10000 --require ts-node/register **/*.spec.ts` | 
| [nomiclabs/buidler](https://github.com/nomiclabs/buidler) | 160 | `nyc mocha` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 160 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 159 | `gulp compile && mocha` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 157 | `npm run-script build && mocha --opts test/mocha.opts build/test/config.js build/test` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 157 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 157 | `mocha -r ts-node/register test/*.ts` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 156 | `mocha --require ts-node/register test/**/*.ts` | 
| [cartant/rxjs-marbles](https://github.com/cartant/rxjs-marbles) | 154 | `yarn run lint && yarn run test:build && cross-env FAILING=0 yarn run test:ava && cross-env FAILING=0 yarn run test:jasmine && cross-env FAILING=0 yarn run test:jasmine-angular && cross-env FAILING=0 yarn run test:jest && cross-env FAILING=0 yarn run test:mocha && cross-env FAILING=0 yarn run test:tape` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 152 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 151 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 151 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 148 | `mocha --require espower-typescript/guess "test/**/*.test.ts"` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 145 | `mocha lib/test` | 
| [TrustWallet/trust-ray](https://github.com/TrustWallet/trust-ray) | 144 | `cross-env NODE_ENV=test mocha --recursive --require ts-node/register 'test/**/*.test.ts' --exit` | 
| [calidion/vig](https://github.com/calidion/vig) | 143 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [Soluto/graphql-to-mongodb](https://github.com/Soluto/graphql-to-mongodb) | 143 | `ts-mocha tests/**/*.spec.ts` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 143 | `mocha` | 
| [arfedulov/semantic-ui-calendar-react](https://github.com/arfedulov/semantic-ui-calendar-react) | 142 | `npx cross-env TS_NODE_COMPILER_OPTIONS="{""allowJs"":true}" npx mocha -r ts-node/register ./test/setup.js ./test/**/*.{js,jsx,ts,tsx}` | 
| [vrimar/construct-ui](https://github.com/vrimar/construct-ui) | 141 | `cross-env TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [DotJoshJohnson/vscode-xml](https://github.com/DotJoshJohnson/vscode-xml) | 141 | `npm run compile && mocha ./out/test/**/*.js` | 
| [featurist/hyperdom](https://github.com/featurist/hyperdom) | 141 | `./node_modules/.bin/tsc && npm run karma && npm run mocha && eslint . && npm run tslint` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 141 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 139 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 139 | `mocha` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 138 | `mocha` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 137 | `mocha test/unit/ --exit` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 137 | `TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [Azure/azure-functions-pack](https://github.com/Azure/azure-functions-pack) | 137 | `npm run build && mocha --compilers ts:ts-node/register --recursive test/**/*-spec.ts` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 134 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 134 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [rtfeldman/node-elm-compiler](https://github.com/rtfeldman/node-elm-compiler) | 133 | `rm -rf test/fixtures/elm-stuff && mocha test/**/*.ts --require ts-node/register --watch-extensions ts` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 132 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 132 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [colyseus/colyseus.js](https://github.com/colyseus/colyseus.js) | 132 | `mocha test/*.ts --require ts-node/register` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 130 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 130 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 130 | `TEST_BROWSER_DRIVER=puppeteer meteor test --driver-package=ardatan:mocha --raw-logs` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 129 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 129 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 128 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 128 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 126 | `cross-env NODE_ENV=test mocha --exit` | 
| [prh/prh](https://github.com/prh/prh) | 126 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 126 | `mocha test` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 126 | `mocha --require source-map-support/register dist/test` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 125 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 125 | `istanbul test -- _mocha` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 125 | `mocha --timeout 10000` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 124 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 123 | `mocha --full-trace tests/test.js  --reporter mocha-multi-reporters` | 
| [Esri/react-arcgis](https://github.com/Esri/react-arcgis) | 123 | `nyc mocha` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 122 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 122 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 122 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 119 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 119 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 117 | `mocha --require ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 117 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [googleapis/nodejs-pubsub](https://github.com/googleapis/nodejs-pubsub) | 116 | `nyc mocha build/test` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 114 | `mocha --recursive -t 4000` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 112 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [bpatrik/pigallery2](https://github.com/bpatrik/pigallery2) | 111 | `ng test && mocha --recursive test/backend/unit && mocha --recursive test/backend/integration  && mocha --recursive test/common/unit ` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 111 | `nyc npm run _mocha` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 110 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [nodejs/llparse](https://github.com/nodejs/llparse) | 110 | `npm run mocha && npm run lint` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 110 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 110 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 109 | `npm run lint && npm run prettier && npm run mocha` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 109 | `npm-run-all build test:mocha test:coverage lint` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 109 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 109 | `webpack && mocha-phantomjs test/index.html` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 108 | `nyc mocha --config ./test/.mocharc.yml` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 108 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 108 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 106 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 106 | `mocha -R spec dist/test/**/*.js` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 105 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [wildbit/postmark.js](https://github.com/wildbit/postmark.js) | 105 | `node_modules/mocha/bin/mocha --timeout 10000 --retries 1 -r ts-node/register test/**/*test.ts` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 104 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 104 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 103 | `mocha` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 103 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 103 | `mocha ./spec/*.js` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 103 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 101 | `tsc; mocha --recursive lib/ test/runner` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 101 | `mocha test/* --timeout 500000` | 
| [giantmachines/redux-websocket](https://github.com/giantmachines/redux-websocket) | 100 | `mocha --compilers js:babel-core/register` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 100 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 100 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 100 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 99 | `mocha --ui tdd out/test/extension.test.js` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 98 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 97 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register/type-check 'test/**/*.ts'` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 97 | `node node_modules/mocha/bin/mocha` | 
| [levjj/esverify](https://github.com/levjj/esverify) | 97 | `TS_NODE_TRANSPILE_ONLY=true mocha -r ts-node/register tests/*.ts` | 
| [mtmr0x/nucleo](https://github.com/mtmr0x/nucleo) | 95 | `mocha -r ts-node/register` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 95 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [sunzongzheng/musicApi](https://github.com/sunzongzheng/musicApi) | 94 | `mocha -t 30000 --require @babel/register 'test/*.test.js' --exit` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 93 | `mocha ./dist/test --recursive` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 93 | `mocha` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 92 | `mocha -r ./src/test/common/setup.ts ./lib/src/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 92 | `nyc mocha build/test` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 92 | `mocha test/ --recursive` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 89 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 89 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 88 | `npm run lint && npm run mocha && npm run docs` | 
| [puzzle-js/puzzle-js](https://github.com/puzzle-js/puzzle-js) | 87 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 87 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 87 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 87 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [roblox-ts/roblox-ts](https://github.com/roblox-ts/roblox-ts) | 86 | `npm run build && npx nyc --reporter=html mocha --timeout 0 --recursive out/test.js && lua tests/spec.lua` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 85 | `tsc && mocha "dist/test/**/*.js" ` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 85 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 85 | `mocha --require ts-node/register test/**/*.ts` | 
| [googleapis/nodejs-datastore](https://github.com/googleapis/nodejs-datastore) | 85 | `nyc mocha build/test` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 84 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 83 | `mocha --timeout 10000 --slow 2500 tests/unittests/**/*.spec.js tests/functional-test-cases.js` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 83 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 82 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 82 | `mocha --compilers js:babel-core/register --recursive` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 81 | `mocha` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [teambition/ReactiveDB](https://github.com/teambition/ReactiveDB) | 80 | `npm run lint && NODE_ENV=test tman --mocha spec-js/test/run.js` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 79 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 78 | `mocha -u tdd ./out/tests/` | 
| [rpgeeganage/async-ray](https://github.com/rpgeeganage/async-ray) | 78 | `nyc mocha` | 
| [CityOfZion/neo-js](https://github.com/CityOfZion/neo-js) | 78 | `mocha --reporter spec` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 78 | `nyc mocha --require ts-node/register test/**/*Test.ts` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 78 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 77 | `mocha -r ts-node/register 'test/main.js'` | 
| [teamdomy/domy](https://github.com/teamdomy/domy) | 77 | `mocha --reporter spec --require ts-node/register 'tests/**/*.spec.ts'` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 77 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 76 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 76 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [balena-io/balena-supervisor](https://github.com/balena-io/balena-supervisor) | 76 | `npm run lint && npm run test:build && JUNIT_REPORT_PATH=report.xml istanbul cover _mocha && npm run coverage` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 76 | `npm run lint && nyc mocha` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 76 | `TS_NODE_FILES=true mocha --opts src/test/mocha.opts "src/test/test*.ts"` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 75 | `nyc mocha --recursive test/**/*.ts` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 75 | `nyc mocha --recursive test/**/*.ts` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 75 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 74 | `yarn run lint && yarn run test:build && yarn run test:mocha` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 74 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 73 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 73 | `npm run compile && mocha && npm run lint` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 73 | `mocha out/**/*.spec.js` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 73 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [WorldBrain/storex](https://github.com/WorldBrain/storex) | 73 | `mocha --require ts-node/register "ts/**/*.test.ts"` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 73 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd './out/test/**/*.test.js'` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 73 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 71 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 71 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 70 | `mocha` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 70 | `nyc mocha` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 70 | `mocha .tmp/spec/index.spec.js` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 70 | `nyc mocha build/test` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 70 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 69 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 69 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [WittBulter/koa2-typescript-guide](https://github.com/WittBulter/koa2-typescript-guide) | 69 | `mocha` | 
| [Cellule/dndGenerator](https://github.com/Cellule/dndGenerator) | 69 | `mocha -r ./mocha-setup src/**/*.spec.ts` | 
| [lukeautry/ts-app](https://github.com/lukeautry/ts-app) | 69 | `cross-env TS_NODE_PROJECT=./api/tsconfig.json mocha -t 15000 -r ts-node/register "./api/**/*.spec.ts"` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 69 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 69 | `nyc mocha` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 68 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 68 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 67 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 67 | `mocha -r ts-node/register test/*.ts` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 66 | `mocha 'lib/**/__tests__/*.js'` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 65 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [mysticatea/regexpp](https://github.com/mysticatea/regexpp) | 65 | `nyc _mocha "test/*.ts" --reporter dot --timeout 10000` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 65 | `mocha build/tests/index.js` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 65 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [demipixel/factorio-blueprint](https://github.com/demipixel/factorio-blueprint) | 64 | `mocha` | 
| [ngduc/node-rem](https://github.com/ngduc/node-rem) | 64 | `cross-env NODE_ENV=test nyc --reporter=html --reporter=text --reporter=lcov mocha --require ts-node/register --full-trace --bail --timeout 20000 --exit tests/**/*.ts` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 64 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 64 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 64 | `mocha --timeout 99999999 --exit -r ts-node/register test/**/*.spec.ts` | 
| [demipixel/factorio-blueprint](https://github.com/demipixel/factorio-blueprint) | 64 | `mocha` | 
| [ngduc/node-rem](https://github.com/ngduc/node-rem) | 64 | `cross-env NODE_ENV=test nyc --reporter=html --reporter=text --reporter=lcov mocha --require ts-node/register --full-trace --bail --timeout 20000 --exit tests/**/*.ts` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 64 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 64 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 64 | `mocha --timeout 99999999 --exit -r ts-node/register test/**/*.spec.ts` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 63 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 63 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [JustClear/colority](https://github.com/JustClear/colority) | 63 | `mocha test/index.js` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 63 | `mocha --opts test/mocha.opts` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 63 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [nhabuiduc/react-filter-box](https://github.com/nhabuiduc/react-filter-box) | 63 | `node --max-old-space-size=16000 ./node_modules/.bin/mocha-webpack --require ignore-styles -r jsdom-global/register --webpack-config webpack.test.config.js --watch "./test/**/*.ts"` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 62 | `node_modules/.bin/mocha --watch` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 62 | `mocha out/test` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 62 | `mocha dist/test/*.js` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 61 | `mocha test/*.js` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [angular-extensions/model](https://github.com/angular-extensions/model) | 61 | `npm run lint && npm run format:test && nyc mocha {lib,schematics}/**/*.test.ts --require ts-node/register --require source-map-support/register` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 61 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 60 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 60 | `mocha --timeout 30000 test/**/*.js` | 
| [wix/rawss](https://github.com/wix/rawss) | 60 | `mocha` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 60 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 60 | `nyc mocha` | 
| [balmbees/dynamo-types](https://github.com/balmbees/dynamo-types) | 60 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 59 | `tsc --version && tsc && mocha out/test` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 59 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 58 | `npm run compile && mocha` | 
| [yesmeck/waque](https://github.com/yesmeck/waque) | 58 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 58 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 58 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [hg-pyun/iterize](https://github.com/hg-pyun/iterize) | 58 | `mocha --recursive ./test/*.ts --require ts-node/register` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 58 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 58 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [mono/TsToCSharp](https://github.com/mono/TsToCSharp) | 58 | `npm run lint && mocha  ./dist/TsToCSharpTests.js` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 57 | `cross-env NODE_ENV=test mocha` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 57 | `mocha` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 57 | `mocha` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 57 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 56 | `mocha --ui qunit` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 56 | `mocha --recursive --reporter-options mochaFile=report.xml --reporter mocha-junit-reporter` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [weaveworks/promjs](https://github.com/weaveworks/promjs) | 55 | `mocha --recursive "test/**/*-test.ts"` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 55 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 54 | `mocha --opts config/mocha.opts` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 54 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 54 | `npm run build && npm run mocha` | 
| [asakusuma/swae](https://github.com/asakusuma/swae) | 54 | `yarn build && rm -rf test/dist && yarn run lint && yarn run build-test && mocha test/dist/test/**/*.spec.js --timeout 15000` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 54 | `nyc mocha` | 
| [rpgeeganage/ifto](https://github.com/rpgeeganage/ifto) | 54 | `nyc mocha` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 54 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 54 | `nyc mocha --opts test/mocha.opts` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 53 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 53 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 53 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [desertkun/hiera-editor](https://github.com/desertkun/hiera-editor) | 53 | `mocha --timeout 15000 dist/tests/**/*.js` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 53 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 53 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 53 | `cross-env TS_NODE_FILES=true nyc mocha test/**/*.ts` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 52 | `NODE_ENV=test nyc mocha` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 52 | `NODE_ENV=test nyc mocha` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 52 | `npm run compile && mocha && npm run lint` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 52 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 52 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 52 | `mocha` | 
| [VoxaAI/voxa](https://github.com/VoxaAI/voxa) | 52 | `mocha test/*.spec.* test/**/*.spec.*` | 
| [jackrobertscott/graphql-api-demo](https://github.com/jackrobertscott/graphql-api-demo) | 52 | `NODE_ENV=test mocha --require=ts-node/register --recursive --exit 'src/**/*.spec.ts'` | 
| [WittBulter/todo-live](https://github.com/WittBulter/todo-live) | 52 | `mocha` | 
| [Microsoft/vscode-html-languageservice](https://github.com/Microsoft/vscode-html-languageservice) | 51 | `npm run compile && mocha && npm run lint` | 
| [strongloop/loopback4-example-shopping](https://github.com/strongloop/loopback4-example-shopping) | 51 | `lb-mocha --allow-console-logs "dist/test"` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 51 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 51 | `mocha --require ts-node/register tests/**/*.ts` | 
| [Microsoft/vscode-html-languageservice](https://github.com/Microsoft/vscode-html-languageservice) | 51 | `npm run compile && mocha && npm run lint` | 
| [strongloop/loopback4-example-shopping](https://github.com/strongloop/loopback4-example-shopping) | 51 | `lb-mocha --allow-console-logs "dist/test"` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 51 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 51 | `mocha --require ts-node/register tests/**/*.ts` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 51 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 51 | `cross-env NODE_ENV=test mocha test/**/*.ts` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [Grademark/grademark](https://github.com/Grademark/grademark) | 51 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 50 | `mocha --opts mocha.opts --watch` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 50 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [BeTomorrow/ReImproveJS](https://github.com/BeTomorrow/ReImproveJS) | 50 | `mocha --reporter spec --compilers ts:ts-node/register 'test/*.spec.ts' --timeout 120000` | 
| [voodooattack/serialism](https://github.com/voodooattack/serialism) | 50 | `nyc mocha --expose-gc --ui mocha-typescript test/test_**.ts` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 50 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 50 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [teppeis/closure-ts](https://github.com/teppeis/closure-ts) | 50 | `npm-run-all --aggregate-output -p lint:ts build -p lint:js mocha` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 49 | `mocha --compilers ts:ts-node/register --recursive` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 49 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 49 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 48 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 48 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 48 | `mocha` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [RobinCK/typeorm-fixtures](https://github.com/RobinCK/typeorm-fixtures) | 48 | `nyc mocha` | 
| [SPGoding/spu](https://github.com/SPGoding/spu) | 48 | `mocha --require espower-typescript/guess "./src/test/**/*.ts"` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 47 | `mocha --opts cli-test-mocha.opts` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 47 | `mocha --recursive` | 
| [NativeScript/nativescript-dev-appium](https://github.com/NativeScript/nativescript-dev-appium) | 47 | `mocha --timeout 999999` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 47 | `nyc mocha build/test` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 47 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 46 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [eclipse/sprotty](https://github.com/eclipse/sprotty) | 46 | `jenkins-mocha --opts ./configs/mocha.opts "./src/**/*.spec.?(ts|tsx)"` | 
| [ProjectOpenSea/opensea-js](https://github.com/ProjectOpenSea/opensea-js) | 45 | `./node_modules/.bin/mocha test/*.ts --require ts-node/register --timeout 15000` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 45 | `npm run lint && mocha dist/spec` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 45 | `mocha out/{,**/}*.spec.js -s 0` | 
| [ethereum-ts/evm-ts](https://github.com/ethereum-ts/evm-ts) | 45 | `yarn lint && yarn test:mocha` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 45 | `mocha -R spec ./test` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 45 | `mocha test` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 45 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 44 | `node_modules/.bin/mocha` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 44 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [sourcegraph/browser-extensions](https://github.com/sourcegraph/browser-extensions) | 44 | `mocha --require ts-node/register --watch --watch-extensions ts './src/**/*.test.ts?(x)'` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 44 | `mocha && npm run aplus` | 
| [pokemongo-dev-contrib/pokemongo-json-pokedex](https://github.com/pokemongo-dev-contrib/pokemongo-json-pokedex) | 44 | `mocha --recursive --compilers ts:ts-node/register,ts:tsconfig-paths/register test/*.ts test/**/*.ts` | 
| [olivierlsc/swagger-express-ts](https://github.com/olivierlsc/swagger-express-ts) | 44 | `echo "Testing..." && npm run build && nyc mocha` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 44 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 44 | `atool-test-mocha ./src/**/*-test.js` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 44 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 43 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [Jiasm/typescript-example](https://github.com/Jiasm/typescript-example) | 43 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [Pushwoosh/web-push-notifications](https://github.com/Pushwoosh/web-push-notifications) | 43 | `mocha` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 43 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 43 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 43 | `tsc && mocha build/test` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 42 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [gcanti/hyper-ts](https://github.com/gcanti/hyper-ts) | 42 | `npm run prettier && npm run lint && npm run typings-checker && npm run mocha` | 
| [NEEOInc/neeo-sdk](https://github.com/NEEOInc/neeo-sdk) | 42 | `TS_NODE_PROJECT=./test/tsconfig.json nyc mocha ./test/**/*.ts --opts ./test/mocha.opts` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 42 | `tsc && mocha spec/` | 
| [FontoXML/fontoxpath](https://github.com/FontoXML/fontoxpath) | 42 | `ts-mocha --require test/testhook.js "test/specs/**/*.ts"` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 41 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 41 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 41 | `mocha` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 41 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 41 | `mocha index.test.js` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 41 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 41 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 40 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 40 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [shogogg/ts-option](https://github.com/shogogg/ts-option) | 40 | `mocha --reporter spec --compilers ts:espower-typescript/guess` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 40 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 40 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [azu/localstorage-ponyfill](https://github.com/azu/localstorage-ponyfill) | 40 | `mocha "test/**/*.ts"` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 40 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 39 | `mocha --opts ./mocha.opts` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 39 | `tsc && npm run lint && mocha` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 39 | `tsc && mocha dist/**/*.spec.js` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 39 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [josephg/statecraft](https://github.com/josephg/statecraft) | 39 | `mocha -r ts-node/register test/*.ts` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 39 | `mocha test/*.spec.ts` | 
| [RocketChat/Rocket.Chat.js.SDK](https://github.com/RocketChat/Rocket.Chat.js.SDK) | 39 | `nyc mocha './src/lib/**/*.spec.ts'` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 39 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 39 | `mocha --recursive "dist/**/*.test.js"` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 39 | `npm run mocha && npm run lint` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 39 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [bromne/typescript-optional](https://github.com/bromne/typescript-optional) | 39 | `nyc mocha src/*` | 
| [DanielSchaffer/webpack-babel-multi-target-plugin](https://github.com/DanielSchaffer/webpack-babel-multi-target-plugin) | 38 | `TS_NODE_PROJECT=tsconfig.spec.json TS_NODE_FILES=true mocha src/**/*.spec.ts` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 38 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [konvajs/ng2-konva](https://github.com/konvajs/ng2-konva) | 38 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [juliantellez/lambcycle](https://github.com/juliantellez/lambcycle) | 38 | `mocha --opts config/mocha/mocha.opts` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 38 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 38 | `tsc -p .tsconfig.test.json && mocha` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 38 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [tbluemel/rtf.js](https://github.com/tbluemel/rtf.js) | 38 | `mocha test/test.js` | 