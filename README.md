# Find Repos in TypeScript Tested using Mocha

The list was updated at 01:56:19 01/30/19 PST

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 68174 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 16862 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 12126 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 10696 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 7104 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 6382 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 5590 | `npm run mocha` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4682 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4634 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 4471 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [rrweb-io/rrweb](https://github.com/rrweb-io/rrweb) | 3685 | `npm run bundle:browser && cross-env TS_NODE_CACHE=false TS_NODE_FILES=true mocha -r ts-node/register test/**/*.test.ts` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3412 | `mocha --opts mocha.opts` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 3053 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2919 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2872 | `mocha` | 
| [electron-userland/electron-forge](https://github.com/electron-userland/electron-forge) | 2540 | `cross-env TS_NODE_FILES=true yarn run mocha './tools/test-globber.ts' --opts mocha.opts` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2443 | `mocha 'test/**/*.ts'` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2280 | `mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [benjamn/recast](https://github.com/benjamn/recast) | 2199 | `npm run tsc && npm run mocha` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1916 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1901 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1812 | `mocha` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1779 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1461 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [colyseus/colyseus](https://github.com/colyseus/colyseus) | 1449 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1426 | `nyc -x '' mocha` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 1382 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [shanalikhan/code-settings-sync](https://github.com/shanalikhan/code-settings-sync) | 1345 | `npm run tslint-check && tsc -p ./ && mocha --recursive "./out/test/**/*.js"` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1286 | `mocha --opts mocha.opts` | 
| [cherow/cherow](https://github.com/cherow/cherow) | 1263 | `cross-env TS_NODE_PROJECT="test/tsconfig.json" mocha "test/**/*.ts" -c -R progress -r ts-node/register -r source-map-support/register --recursive --globals expect` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1231 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [funkia/list](https://github.com/funkia/list) | 1230 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1223 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [google/clasp](https://github.com/google/clasp) | 1214 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1139 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1107 | `nyc --reporter=html --reporter=text mocha` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 1071 | `tsc -p ./ && mocha` | 
| [itchio/itch](https://github.com/itchio/itch) | 1012 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 947 | `mocha --opts test/mocha.opts` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 931 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 922 | `mocha bin/tests/test.js` | 
| [netgusto/nodebook](https://github.com/netgusto/nodebook) | 776 | `mocha test/backend` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 768 | `mocha --require ts-node/register` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 738 | `yarn run lint && yarn run test:mocha` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 728 | `mocha` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 719 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 714 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 713 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 700 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 673 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 645 | `mocha --recursive` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 628 | `mocha "out/**/*.spec.js" -s 0` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 613 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 608 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 605 | `mocha test/unit` | 
| [JustClear/blurify](https://github.com/JustClear/blurify) | 597 | `mocha test/index.js` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 593 | `npm run lint && npm run mocha` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 588 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 585 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [googleapis/google-auth-library-nodejs](https://github.com/googleapis/google-auth-library-nodejs) | 581 | `nyc mocha build/test` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 581 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 580 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 566 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 560 | `mocha` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 559 | `mocha test` | 
| [dsherret/ts-simple-ast](https://github.com/dsherret/ts-simple-ast) | 546 | `cross-env TS_NODE_COMPILER="ttypescript" TS_NODE_TRANSPILE_ONLY="true" mocha --opts mocha.opts --grep @performance --invert` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 539 | `mocha --opts test/mocha.opts dist/test` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 528 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [benjamn/ast-types](https://github.com/benjamn/ast-types) | 499 | `npm run gen && npm run tsc && npm run mocha` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 499 | `cross-env NODE_ENV=tsoa_test mocha **/*.spec.ts --exit --compilers ts:ts-node/register` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 493 | `mocha --opts mocha.opts` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 490 | `mocha --opts mocha.opts` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 483 | `tsc && mocha test && yarn lint` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 482 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 478 | `npm run mocha` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 478 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 472 | `cd test && mocha -r ts-node/register *.ts` | 
| [Cookie-AutoDelete/Cookie-AutoDelete](https://github.com/Cookie-AutoDelete/Cookie-AutoDelete) | 469 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec ./test/*` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 462 | `npm run build && mocha` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 458 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 450 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 444 | `_mocha --` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 429 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 412 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 404 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 393 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 383 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [R-js/libRmath.js](https://github.com/R-js/libRmath.js) | 380 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 361 | `mocha` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 358 | `npm run build && mocha` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 350 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [Microsoft/node-pty](https://github.com/Microsoft/node-pty) | 350 | `cross-env NODE_ENV=test mocha -R spec --exit lib/*.test.js` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 345 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 343 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 335 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 328 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 320 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 318 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts extension/test/test-*.ts view/test/test-heightmap.ts` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 315 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 312 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 311 | `mocha` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 304 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 298 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 292 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 291 | `mocha` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 289 | `mocha lib/test` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 279 | `mocha --compilers js:babel-register test/**/*.js` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 278 | `mocha` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 273 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 272 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec --bail` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 267 | `mocha src/**/*.spec.ts` | 
| [juanfranblanco/vscode-solidity](https://github.com/juanfranblanco/vscode-solidity) | 265 | `mocha -r ts-node/register test/*.spec.ts` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 257 | `mocha "test/**/*.spec.ts"` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 255 | `tsc && mocha dist/**/*.spec.js` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 251 | `mocha-webpack "src/**/*.ts"` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 251 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 251 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [AmirTugi/tea-school](https://github.com/AmirTugi/tea-school) | 248 | `npx ts-mocha ./src/tests/**.ts` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 248 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 245 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 245 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 237 | `tsc && mocha` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 233 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 226 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 226 | `nyc --reporter html mocha` | 
| [googleapis/nodejs-storage](https://github.com/googleapis/nodejs-storage) | 224 | `nyc mocha build/test` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 223 | `cd test && mocha -r ts-node/register *.ts` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 215 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 212 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | 212 | `nyc mocha` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 210 | `mocha test` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 208 | `cross-env NODE_ENV=test mocha --exit` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 207 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 207 | `mocha dist/test.js` | 
| [Zarel/Pokemon-Showdown-Client](https://github.com/Zarel/Pokemon-Showdown-Client) | 203 | `eslint --config=.eslintrc.js --cache --cache-file=eslint-cache/base js/ data/ && eslint --config=build-tools/.eslintrc.js --cache --cache-file=eslint-cache/build build-tools/update build-tools/build-indexes && tslint --project . && tsc && node build && mocha` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 202 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [R-js/blasjs](https://github.com/R-js/blasjs) | 202 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [bmewburn/intelephense](https://github.com/bmewburn/intelephense) | 200 | `mocha -r ts-node/register test/*.ts` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 200 | `mocha -R spec test/integration` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 197 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 190 | `mocha js` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 190 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 190 | `mocha lib/spec/core` | 
| [Odi-ts/odi](https://github.com/Odi-ts/odi) | 187 | `nyc mocha test/**/*.test.ts --exit` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 186 | `nyc mocha --recursive test/**/*.ts` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 185 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 180 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 179 | `npm run build && npm run mocha` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 173 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [emmanueltouzery/prelude-ts](https://github.com/emmanueltouzery/prelude-ts) | 173 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 173 | `npm run lint && npm run mocha` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 172 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 172 | `tsc && cd dist && mocha` | 
| [Chinachu/Mirakurun](https://github.com/Chinachu/Mirakurun) | 168 | `mocha --exit test/*.spec.js` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 166 | `npm run clean && npm run build && npm run lint && mocha` | 
| [nodejs/llhttp](https://github.com/nodejs/llhttp) | 163 | `npm run mocha && npm run lint` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 161 | `gulp compile && mocha --timeout 10000 -u tdd ./out/tests/` | 
| [googleapis/nodejs-translate](https://github.com/googleapis/nodejs-translate) | 158 | `nyc mocha build/test` | 
| [PeterDing/chord](https://github.com/PeterDing/chord) | 157 | `./node_modules/mocha/bin/mocha --delay` | 
| [p-society/typeracer-cli](https://github.com/p-society/typeracer-cli) | 156 | `mocha --no-deprecation --timeout 10000 --require ts-node/register **/*.spec.ts` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 155 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 153 | `mocha --require ts-node/register test/**/*.ts` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 152 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 152 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 151 | `tsc && mocha` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 151 | `gulp compile && mocha` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 151 | `mocha -r ts-node/register test/*.ts` | 
| [Microsoft/typescript-tslint-plugin](https://github.com/Microsoft/typescript-tslint-plugin) | 148 | `mocha ./out/**/*.test.js --slow 2000 --timeout 10000` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 148 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 146 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [calidion/vig](https://github.com/calidion/vig) | 145 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 145 | `nyc --reporter=html --reporter=text mocha` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 142 | `mocha lib/test` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 141 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [rtfeldman/node-elm-compiler](https://github.com/rtfeldman/node-elm-compiler) | 131 | `rm -rf test/fixtures/elm-stuff && mocha test/**/*.ts --require ts-node/register --watch-extensions ts` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 130 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 130 | `TEST_BROWSER_DRIVER=puppeteer meteor test --driver-package=ardatan:mocha --raw-logs` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 129 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 129 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 128 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 127 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 125 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 125 | `mocha --require source-map-support/register dist/test` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 124 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 124 | `istanbul test -- _mocha` | 
| [prh/prh](https://github.com/prh/prh) | 124 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 124 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 124 | `mocha test` | 
| [rtfeldman/node-elm-compiler](https://github.com/rtfeldman/node-elm-compiler) | 131 | `rm -rf test/fixtures/elm-stuff && mocha test/**/*.ts --require ts-node/register --watch-extensions ts` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 130 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 130 | `TEST_BROWSER_DRIVER=puppeteer meteor test --driver-package=ardatan:mocha --raw-logs` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 129 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 129 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 128 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 127 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [arfedulov/semantic-ui-calendar-react](https://github.com/arfedulov/semantic-ui-calendar-react) | 126 | `npx cross-env TS_NODE_COMPILER_OPTIONS="{""allowJs"":true}" npx mocha -r ts-node/register ./test/setup.js ./test/**/*.{js,jsx,ts,tsx}` | 
| [colyseus/colyseus.js](https://github.com/colyseus/colyseus.js) | 126 | `mocha test/*.ts --require ts-node/register` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 125 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 125 | `mocha --require source-map-support/register dist/test` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 124 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 124 | `istanbul test -- _mocha` | 
| [prh/prh](https://github.com/prh/prh) | 124 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 124 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 124 | `mocha test` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 124 | `mocha --timeout 10000` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 122 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 122 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 120 | `cross-env NODE_ENV=test mocha --exit` | 
| [nomiclabs/buidler](https://github.com/nomiclabs/buidler) | 120 | `nyc mocha` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 119 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 119 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 119 | `mocha` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 118 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 116 | `npm run lint && node_modules/.bin/nyc --require source-map-support/register npm run mocha` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 116 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 116 | `npm run lint && node_modules/.bin/nyc --require source-map-support/register npm run mocha` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 116 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 113 | `mocha --full-trace tests/test.js  --reporter mocha-multi-reporters` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 112 | `mocha --recursive -t 4000` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 112 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 112 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 111 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 111 | `TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [Esri/react-arcgis](https://github.com/Esri/react-arcgis) | 111 | `nyc mocha` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 110 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 110 | `webpack && mocha-phantomjs test/index.html` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 108 | `mocha --require ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 108 | `npm-run-all build test:mocha test:coverage lint` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 107 | `mocha -R spec dist/test/**/*.js` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 107 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 106 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 105 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 104 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 104 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 104 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 103 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 103 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 102 | `mocha` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 102 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 102 | `nyc npm run _mocha` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 102 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [nodejs/llparse](https://github.com/nodejs/llparse) | 101 | `npm run mocha && npm run lint` | 
| [wildbit/postmark.js](https://github.com/wildbit/postmark.js) | 101 | `node_modules/mocha/bin/mocha --timeout 10000 --retries 1 -r ts-node/register test/**/*test.ts` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 101 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 100 | `npm run lint && npm run prettier && npm run mocha` | 
| [googleapis/nodejs-pubsub](https://github.com/googleapis/nodejs-pubsub) | 100 | `nyc mocha build/test` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 99 | `tsc; mocha --recursive lib/ test/runner` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 98 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 97 | `mocha ./spec/*.js` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 97 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 97 | `mocha test/* --timeout 500000` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 96 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 96 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [nucleojs/nucleo](https://github.com/nucleojs/nucleo) | 95 | `mocha -r ts-node/register` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 95 | `node node_modules/mocha/bin/mocha` | 
| [levjj/esverify](https://github.com/levjj/esverify) | 95 | `TS_NODE_TRANSPILE_ONLY=true mocha -r ts-node/register tests/*.ts` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 94 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register/type-check 'test/**/*.ts'` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 94 | `mocha ./dist/test --recursive` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 93 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 92 | `mocha` | 
| [bpatrik/pigallery2](https://github.com/bpatrik/pigallery2) | 91 | `ng test && mocha --recursive test/backend/unit && mocha --recursive test/backend/integration  && mocha --recursive test/common/unit ` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 91 | `mocha test/ --recursive` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 89 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 89 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 88 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 87 | `mocha -r ./src/test/common/setup.ts ./lib/src/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 87 | `mocha --ui tdd out/test/extension.test.js` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 86 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 85 | `nyc mocha` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 84 | `nyc mocha build/test` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 84 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 84 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 83 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 83 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 82 | `mocha --require ts-node/register test/**/*.ts` | 
| [woutervh-/typescript-is](https://github.com/woutervh-/typescript-is) | 81 | `npm run lint && npm run build && ttsc --project tsconfig-test.json && mocha` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 81 | `mocha` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 79 | `tsc && mocha "dist/test/**/*.js" ` | 
| [rpgeeganage/async-ray](https://github.com/rpgeeganage/async-ray) | 79 | `nyc mocha` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 79 | `mocha --compilers js:babel-core/register --recursive` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 79 | `npm run lint && npm run mocha` | 
| [teambition/ReactiveDB](https://github.com/teambition/ReactiveDB) | 78 | `npm run lint && NODE_ENV=test tman --mocha spec-js/test/run.js` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 78 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [CityOfZion/neo-js](https://github.com/CityOfZion/neo-js) | 78 | `mocha --reporter spec` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 77 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 77 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 77 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 76 | `npm run lint && nyc mocha` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 76 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 75 | `nyc mocha --recursive test/**/*.ts` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 75 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 74 | `mocha -r ts-node/register 'test/main.js'` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 74 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 73 | `mocha -u tdd ./out/tests/` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 73 | `mocha out/**/*.spec.js` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 73 | `TS_NODE_FILES=true mocha --opts src/test/mocha.opts "src/test/test*.ts"` | 
| [roblox-ts/roblox-ts](https://github.com/roblox-ts/roblox-ts) | 73 | `nyc --reporter=html mocha --timeout 0 --require ts-node/register --require source-map-support/register --recursive src/test.ts && lua tests/spec.lua` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 72 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 72 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 71 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 71 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 71 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 70 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [puzzle-js/puzzle-js](https://github.com/puzzle-js/puzzle-js) | 69 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 69 | `npm run compile && mocha && npm run lint` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 69 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 69 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 68 | `mocha --opts spec/mocha.opts spec/**/*-spec.ts` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 68 | `mocha --opts spec/mocha.opts spec/**/*-spec.ts` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 68 | `mocha .tmp/spec/index.spec.js` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 68 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 67 | `mocha -r ts-node/register test/*.ts` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 66 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 66 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd ./out/test/extension.test.js` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 65 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 64 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 64 | `nyc mocha build/test` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 64 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 64 | `nyc mocha` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 63 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 63 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 63 | `mocha 'lib/**/__tests__/*.js'` | 
| [teamdomy/domy](https://github.com/teamdomy/domy) | 63 | `mocha --reporter spec --require ts-node/register 'tests/**/*.spec.ts'` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 62 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [JustClear/colority](https://github.com/JustClear/colority) | 62 | `mocha test/index.js` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 62 | `nyc mocha --opts .mocha.opts` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 62 | `mocha dist/test/*.js` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 61 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 61 | `mocha build/tests/index.js` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 61 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 61 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 60 | `mocha` | 
| [DhyanaChina/koa2-typescript-guide](https://github.com/DhyanaChina/koa2-typescript-guide) | 60 | `mocha` | 
| [wix/rawss](https://github.com/wix/rawss) | 60 | `mocha` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 60 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [lukeautry/ts-app](https://github.com/lukeautry/ts-app) | 59 | `cross-env TS_NODE_PROJECT=./api/tsconfig.json mocha -t 15000 -r ts-node/register "./api/**/*.spec.ts"` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 59 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 58 | `node_modules/.bin/mocha --watch` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 58 | `mocha --timeout 30000 test/**/*.js` | 
| [mono/TsToCSharp](https://github.com/mono/TsToCSharp) | 58 | `npm run lint && mocha  ./dist/TsToCSharpTests.js` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 57 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 57 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 57 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 57 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [nhabuiduc/react-filter-box](https://github.com/nhabuiduc/react-filter-box) | 57 | `node --max-old-space-size=16000 ./node_modules/.bin/mocha-webpack --require ignore-styles -r jsdom-global/register --webpack-config webpack.test.config.js --watch "./test/**/*.ts"` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 57 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 56 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 56 | `mocha` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 56 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 55 | `npm run compile && mocha` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 55 | `mocha out/test` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 55 | `mocha --recursive --reporter-options mochaFile=report.xml --reporter mocha-junit-reporter` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 54 | `npm run build && npm run mocha` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 54 | `mocha --opts test/mocha.opts` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 54 | `tsc --version && tsc && mocha out/test` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 54 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 53 | `mocha --ui qunit` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 53 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 53 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [asakusuma/swae](https://github.com/asakusuma/swae) | 53 | `yarn build && rm -rf test/dist && yarn run lint && yarn run build-test && mocha test/dist/test/**/*.spec.js --timeout 15000` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 53 | `mocha` | 
| [hg-pyun/iterize](https://github.com/hg-pyun/iterize) | 53 | `mocha --recursive ./test/*.ts --require ts-node/register` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 53 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 53 | `nyc mocha` | 
| [balmbees/dynamo-types](https://github.com/balmbees/dynamo-types) | 53 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 53 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 52 | `mocha` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 52 | `NODE_ENV=test nyc mocha` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 52 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 52 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 52 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 52 | `nyc mocha` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 51 | `mocha test/*.js` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 51 | `NODE_ENV=test nyc mocha` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 51 | `npm run compile && mocha && npm run lint` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 51 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [DhyanaChina/todo-live](https://github.com/DhyanaChina/todo-live) | 51 | `mocha` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 50 | `mocha --opts config/mocha.opts` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 50 | `cross-env NODE_ENV=test mocha` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [voodooattack/serialism](https://github.com/voodooattack/serialism) | 50 | `nyc mocha --expose-gc --ui mocha-typescript test/test_**.ts` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [VoxaAI/voxa](https://github.com/VoxaAI/voxa) | 50 | `mocha test/*.spec.* test/**/*.spec.*` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 50 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 49 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 49 | `mocha --opts mocha.opts --watch` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 49 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 49 | `mocha --compilers ts:ts-node/register --recursive` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 49 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [aykutkardas/Json-Function](https://github.com/aykutkardas/Json-Function) | 49 | `cross-env TS_NODE_COMPILER_OPTIONS='{ "module": "commonjs" }' mocha -r ts-node/register -r ignore-styles -r jsdom-global/register test/**/*.spec.ts` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 49 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 49 | `mocha --reporter spec` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 49 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 49 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 49 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [teppeis/closure-ts](https://github.com/teppeis/closure-ts) | 49 | `npm-run-all --aggregate-output -p lint:ts build -p lint:js mocha` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 48 | `mocha --require ts-node/register tests/**/*.ts` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 48 | `cross-env NODE_ENV=test mocha test/**/*.ts` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 48 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [SPGoding/spu](https://github.com/SPGoding/spu) | 48 | `mocha --require espower-typescript/guess "./src/test/**/*.ts"` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 48 | `nyc mocha --opts test/mocha.opts` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 47 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [BeTomorrow/ReImproveJS](https://github.com/BeTomorrow/ReImproveJS) | 47 | `mocha --reporter spec --compilers ts:ts-node/register 'test/*.spec.ts' --timeout 120000` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 47 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [Grademark/grademark](https://github.com/Grademark/grademark) | 47 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 46 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [NativeScript/nativescript-dev-appium](https://github.com/NativeScript/nativescript-dev-appium) | 46 | `mocha --timeout 999999` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 46 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [NativeScript/nativescript-dev-appium](https://github.com/NativeScript/nativescript-dev-appium) | 46 | `mocha --timeout 999999` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 46 | `nyc mocha --require source-map-support/register --require ts-node/register test/**/*.ts` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 45 | `mocha --opts cli-test-mocha.opts` | 
| [yesmeck/waque](https://github.com/yesmeck/waque) | 45 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 45 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 45 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 45 | `mocha -R spec ./test` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 45 | `mocha test` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 44 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 44 | `npm run lint && mocha dist/spec` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 44 | `mocha out/{,**/}*.spec.js -s 0` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 44 | `mocha --recursive` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 44 | `nyc mocha build/test` | 
| [sourcegraph/browser-extensions](https://github.com/sourcegraph/browser-extensions) | 44 | `mocha --require ts-node/register --watch --watch-extensions ts './src/**/*.test.ts?(x)'` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 44 | `mocha` | 
| [rpgeeganage/ifto](https://github.com/rpgeeganage/ifto) | 44 | `nyc mocha` | 
| [jackrobertscott/graphql-api-demo](https://github.com/jackrobertscott/graphql-api-demo) | 44 | `NODE_ENV=test mocha --require=ts-node/register --recursive --exit 'src/**/*.spec.ts'` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 43 | `node_modules/.bin/mocha` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 43 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 43 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [ethereum-ts/evm-ts](https://github.com/ethereum-ts/evm-ts) | 43 | `yarn lint && yarn test:mocha` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 43 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 43 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 43 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 43 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 43 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 42 | `mocha && npm run aplus` | 
| [Pushwoosh/web-push-notifications](https://github.com/Pushwoosh/web-push-notifications) | 42 | `mocha` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 42 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 41 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [Jiasm/typescript-example](https://github.com/Jiasm/typescript-example) | 41 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 41 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [olivierlsc/swagger-express-ts](https://github.com/olivierlsc/swagger-express-ts) | 41 | `echo "Testing..." && npm run build && nyc mocha` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 41 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 41 | `tsc && mocha build/test` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 41 | `mocha index.test.js` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 41 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 41 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 40 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 40 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [pokemongo-dev-contrib/pokemongo-json-pokedex](https://github.com/pokemongo-dev-contrib/pokemongo-json-pokedex) | 40 | `mocha --recursive --compilers ts:ts-node/register,ts:tsconfig-paths/register test/*.ts test/**/*.ts` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 40 | `atool-test-mocha ./src/**/*-test.js` | 
| [webix-hub/webix-jet](https://github.com/webix-hub/webix-jet) | 40 | `webpack && phantomjs node_modules/mocha-phantomjs-core/mocha-phantomjs-core.js tests/index.html spec` | 
| [FontoXML/fontoxpath](https://github.com/FontoXML/fontoxpath) | 40 | `ts-mocha --require test/testhook.js "test/specs/**/*.ts"` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 39 | `tsc && npm run lint && mocha` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 39 | `mocha --opts ./mocha.opts` | 
| [azu/localstorage-ponyfill](https://github.com/azu/localstorage-ponyfill) | 39 | `mocha "test/**/*.ts"` | 
| [angular-extensions/model](https://github.com/angular-extensions/model) | 39 | `npm run lint && npm run format:test && nyc mocha {lib,schematics}/**/*.test.ts --require ts-node/register --require source-map-support/register` | 
| [gcanti/hyper-ts](https://github.com/gcanti/hyper-ts) | 39 | `npm run prettier && npm run lint && npm run typings-checker && npm run mocha` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 39 | `npm run mocha && npm run lint` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 39 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 39 | `tsc && mocha spec/` | 
| [aurelia/bundler](https://github.com/aurelia/bundler) | 39 | `mocha --reporter spec --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 39 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [ProjectOpenSea/opensea-js](https://github.com/ProjectOpenSea/opensea-js) | 38 | `./node_modules/.bin/mocha test/*.ts --require ts-node/register --timeout 15000` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 38 | `tsc && mocha dist/**/*.spec.js` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 38 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [shogogg/ts-option](https://github.com/shogogg/ts-option) | 38 | `mocha --reporter spec --compilers ts:espower-typescript/guess` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 38 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 37 | `mocha` | 
| [strongloop/loopback4-example-shopping](https://github.com/strongloop/loopback4-example-shopping) | 37 | `lb-mocha --allow-console-logs "dist/test"` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 37 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [acrazing/mobx-sync](https://github.com/acrazing/mobx-sync) | 37 | `mocha --require ts-node/register --slow 1000 ./src/**/*.spec.ts` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 37 | `mocha test/*.spec.ts` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 37 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 37 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 37 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [Webtomizer/typeorm-loader](https://github.com/Webtomizer/typeorm-loader) | 36 | `npm run build && [ -d tests ] && NODE_ENV=test mocha $NODE_DEBUG_OPTION -r ts-node/register -r tslib tests/test_**.ts` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 36 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 36 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 36 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [Polymer/polymer-linter](https://github.com/Polymer/polymer-linter) | 36 | `npm run build && mocha && npm run lint` | 
| [paralin/grpc-bus](https://github.com/paralin/grpc-bus) | 36 | `npm run lint && npm run mocha` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 36 | `mocha --recursive "dist/**/*.test.js"` | 
| [infinum/mobx-collection-store](https://github.com/infinum/mobx-collection-store) | 36 | `NODE_ENV=test nyc mocha` | 
| [bromne/typescript-optional](https://github.com/bromne/typescript-optional) | 36 | `nyc mocha src/*` | 
| [fyndme/messenger-bot-tester](https://github.com/fyndme/messenger-bot-tester) | 35 | `mocha ./test-build` | 
| [tsframework/ts-framework](https://github.com/tsframework/ts-framework) | 35 | `mocha build-test --recursive` | 
| [agea/CmisJS](https://github.com/agea/CmisJS) | 35 | `tsc && mocha dist/**/*.spec.js` | 
| [utopian-io/api.utopian.io](https://github.com/utopian-io/api.utopian.io) | 35 | `cross-env NODE_ENV=test npx mocha --ui bdd --reporter spec --colors --recursive -r ts-node/register tests/index.ts` | 
| [tuzhanai/captcha](https://github.com/tuzhanai/captcha) | 35 | `mocha -b --require ts-node/register --require source-map-support/register --recursive --exit src/test.ts` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 35 | `tsc -p .tsconfig.test.json && mocha` | 
| [ste-vg/pop.svg](https://github.com/ste-vg/pop.svg) | 35 | `nyc mocha --require ./mocha.config.js -r ts-node/register 'src/**/*.spec.ts'  --exit --recursive --timeout 10000` | 
| [Rich-Harris/port-authority](https://github.com/Rich-Harris/port-authority) | 35 | `mocha --opts mocha.opts` | 
| [masvis/angular4-hal](https://github.com/masvis/angular4-hal) | 35 | `mocha -r ts-node/register --config=test/test-config.json test/*.test.ts` | 
| [secret-tech/backend-token-wallets](https://github.com/secret-tech/backend-token-wallets) | 35 | `mocha -r ts-node/register -r test/prepare.ts src/**/*.spec.ts` | 
| [mrmlnc/vscode-stylefmt](https://github.com/mrmlnc/vscode-stylefmt) | 34 | `mocha out/**/*.spec.js -s 0` | 
| [lebinh/cloudflare-workers](https://github.com/lebinh/cloudflare-workers) | 34 | `mocha -r ts-node/register 'tests/**/*_test.ts'` | 
| [Azure/oav](https://github.com/Azure/oav) | 34 | `npm run tsc && npm run tslint && nyc mocha ./dist/test/**/*.js -t 10000 --reporter mocha-junit-reporter --reporter spec` | 
| [leizongmin/leizm-web](https://github.com/leizongmin/leizm-web) | 34 | `npm run format && mocha --require ts-node/register --exit "src/test/**/*.ts"` | 
| [larshp/abaplint](https://github.com/larshp/abaplint) | 34 | `mocha --recursive --reporter progress build/test` | 
| [josephg/statecraft](https://github.com/josephg/statecraft) | 34 | `mocha -r ts-node/register test/*.ts` | 
| [Draccoz/twc](https://github.com/Draccoz/twc) | 34 | `npm run lint && mocha --require ts-node/register --ui bdd tests/tests.spec.ts` | 