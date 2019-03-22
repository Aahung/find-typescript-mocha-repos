# Find Repos in TypeScript Tested using Mocha

The list was updated at 01:57:23 03/22/19 PDT

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 71875 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 17567 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 13678 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 11829 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 7286 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 6696 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 5866 | `npm run mocha` | 
| [peers/peerjs](https://github.com/peers/peerjs) | 5750 | `mocha -r ts-node/register -r jsdom-global/register test/**/*.ts` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 5074 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts && npm run test:packages` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4876 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4872 | `mocha` | 
| [rrweb-io/rrweb](https://github.com/rrweb-io/rrweb) | 4243 | `npm run bundle:browser && cross-env TS_NODE_CACHE=false TS_NODE_FILES=true mocha -r ts-node/register test/**/*.test.ts` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3458 | `mocha --opts mocha.opts` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 3380 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 3131 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [retejs/rete](https://github.com/retejs/rete) | 2983 | `BABEL_ENV=test mocha -r ts-node/register test/**.ts` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2932 | `mocha` | 
| [electron-userland/electron-forge](https://github.com/electron-userland/electron-forge) | 2715 | `cross-env TS_NODE_FILES=true yarn run mocha './tools/test-globber.ts'` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2470 | `mocha 'test/**/*.ts'` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2380 | `mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [benjamn/recast](https://github.com/benjamn/recast) | 2301 | `npm run tsc && npm run mocha` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1977 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1947 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1814 | `mocha` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1802 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [colyseus/colyseus](https://github.com/colyseus/colyseus) | 1615 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 1581 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [shanalikhan/code-settings-sync](https://github.com/shanalikhan/code-settings-sync) | 1540 | `npm run tslint-check && tsc -p ./ && mocha --recursive "./out/test/**/*.js"` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1517 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1511 | `nyc -x '' mocha` | 
| [cherow/cherow](https://github.com/cherow/cherow) | 1465 | `cross-env TS_NODE_PROJECT="test/tsconfig.json" mocha "test/**/*.ts" -c -R progress -r ts-node/register -r source-map-support/register --recursive --globals expect` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1384 | `mocha --opts mocha.opts` | 
| [google/clasp](https://github.com/google/clasp) | 1372 | `nyc --cache false mocha --timeout 100000 -- 'tests/**/*.js'` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1283 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [funkia/list](https://github.com/funkia/list) | 1269 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1227 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [google/gts](https://github.com/google/gts) | 1215 | `nyc mocha build/test` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1189 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1131 | `nyc --reporter=html --reporter=text mocha` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 1126 | `tsc -p ./ && mocha` | 
| [itchio/itch](https://github.com/itchio/itch) | 1039 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 1004 | `mocha bin/tests/test.js` | 
| [youzan/zan-proxy](https://github.com/youzan/zan-proxy) | 1003 | `nyc mocha dist/**/*.spec.js` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 987 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 963 | `mocha --opts test/mocha.opts` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 987 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 963 | `mocha --opts test/mocha.opts` | 
| [stryker-mutator/stryker](https://github.com/stryker-mutator/stryker) | 900 | `npm run mocha` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 817 | `mocha --require ts-node/register` | 
| [NativeScript/nativescript-cli](https://github.com/NativeScript/nativescript-cli) | 812 | `istanbul cover ./node_modules/mocha/bin/_mocha` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 803 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [netgusto/nodebook](https://github.com/netgusto/nodebook) | 790 | `mocha test/backend` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 745 | `yarn run lint && yarn run test:mocha` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 742 | `mocha` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 737 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 737 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 718 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 709 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 684 | `mocha test/unit` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 666 | `mocha "out/**/*.spec.js" -s 0` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 652 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 647 | `mocha --recursive` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 644 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [szokodiakos/typegoose](https://github.com/szokodiakos/typegoose) | 627 | `npm run lint && nyc npm run mocha` | 
| [googleapis/google-auth-library-nodejs](https://github.com/googleapis/google-auth-library-nodejs) | 622 | `nyc mocha build/test` | 
| [dsherret/ts-morph](https://github.com/dsherret/ts-morph) | 618 | `cross-env TS_NODE_COMPILER="ttypescript" TS_NODE_TRANSPILE_ONLY="true" mocha --opts mocha.opts --grep @performance --invert` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 617 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 613 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 611 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 609 | `mocha --opts ./src/test/mocha.opts` | 
| [bbc/sqs-consumer](https://github.com/bbc/sqs-consumer) | 600 | `mocha` | 
| [JustClear/blurify](https://github.com/JustClear/blurify) | 597 | `mocha test/index.js` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 596 | `npm run lint && npm run mocha` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 590 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [mateogianolio/vectorious](https://github.com/mateogianolio/vectorious) | 588 | `nyc mocha -r ts-node/register ./src/*.spec.ts` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 567 | `mocha` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 563 | `mocha test` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 559 | `tsc && mocha test && yarn lint` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 542 | `cd test && mocha -r ts-node/register *.ts` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 537 | `mocha --opts test/mocha.opts dist/test` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 535 | `cross-env NODE_ENV=tsoa_test mocha **/*.spec.ts --exit --compilers ts:ts-node/register` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 531 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 523 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [benjamn/ast-types](https://github.com/benjamn/ast-types) | 515 | `npm run gen && npm run build && npm run mocha` | 
| [Cookie-AutoDelete/Cookie-AutoDelete](https://github.com/Cookie-AutoDelete/Cookie-AutoDelete) | 510 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec ./test/*` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 509 | `mocha --opts mocha.opts` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 508 | `npm run mocha` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 501 | `npm run lint && npm run mocha` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 500 | `mocha --opts mocha.opts` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 496 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 461 | `npm run build && mocha` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 456 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 446 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 445 | `_mocha --` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 431 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 412 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 397 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [amplify-education/serverless-domain-manager](https://github.com/amplify-education/serverless-domain-manager) | 396 | `tsc --project . && nyc mocha -r ts-node/register test/unit-tests/index.test.ts && nyc report --reporter=text-summary` | 
| [aykutkardas/Json-Function](https://github.com/aykutkardas/Json-Function) | 386 | `cross-env TS_NODE_COMPILER_OPTIONS='{ "module": "commonjs" }' mocha -r ts-node/register -r ignore-styles -r jsdom-global/register test/**/*.spec.ts` | 
| [R-js/libRmath.js](https://github.com/R-js/libRmath.js) | 384 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 383 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [Microsoft/node-pty](https://github.com/Microsoft/node-pty) | 382 | `cross-env NODE_ENV=test mocha -R spec --exit lib/*.test.js` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 374 | `npm run build && mocha` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 372 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts extension/test/test-*.ts view/test/test-heightmap.ts` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 368 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 365 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 362 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 360 | `mocha` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 355 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 353 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 350 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 345 | `mocha` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 334 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 332 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 328 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 324 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec --bail` | 
| [alibaba/pont](https://github.com/alibaba/pont) | 323 | `mocha --timeout 15000 -r ts-node/register test/**/test.ts` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 311 | `cd test && mocha -r ts-node/register *.ts` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 305 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 304 | `mocha lib/test` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 300 | `mocha-webpack "src/**/*.ts"` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 293 | `mocha` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 291 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 284 | `mocha` | 
| [nwtgck/piping-server](https://github.com/nwtgck/piping-server) | 283 | `mocha --require ts-node/register --timeout 10000 test/**/*.ts` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 280 | `mocha --compilers js:babel-register test/**/*.js` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 278 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 272 | `tsc && mocha dist/**/*.spec.js` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 272 | `mocha src/**/*.spec.ts` | 
| [juanfranblanco/vscode-solidity](https://github.com/juanfranblanco/vscode-solidity) | 271 | `nyc --require ts-node/register --require source-map-support/register mocha test/**/*.spec.ts` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 270 | `mocha "test/**/*.spec.ts"` | 
| [slothking-online/diagram](https://github.com/slothking-online/diagram) | 270 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | 264 | `nyc mocha` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 261 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [AmirTugi/tea-school](https://github.com/AmirTugi/tea-school) | 257 | `npx ts-mocha ./src/tests/**.ts` | 
| [googleapis/nodejs-storage](https://github.com/googleapis/nodejs-storage) | 256 | `nyc mocha build/test` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 252 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 252 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 250 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 246 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 242 | `tsc && mocha` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 241 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [Odi-ts/odi](https://github.com/Odi-ts/odi) | 236 | `nyc mocha test/**/*.test.ts --exit` | 
| [harttle/liquidjs](https://github.com/harttle/liquidjs) | 229 | `npm run build && mocha "test/**/*.ts"` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 229 | `cross-env NODE_ENV=test mocha --exit` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 226 | `nyc --reporter html mocha` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 224 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 222 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 222 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 216 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 210 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [PeterDing/chord](https://github.com/PeterDing/chord) | 210 | `mocha --delay` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 209 | `mocha test` | 
| [Zarel/Pokemon-Showdown-Client](https://github.com/Zarel/Pokemon-Showdown-Client) | 208 | `eslint --config=.eslintrc.js --cache --cache-file=eslint-cache/base js/ data/ && eslint --config=build-tools/.eslintrc.js --cache --cache-file=eslint-cache/build build-tools/update build-tools/build-indexes && tslint --project . && tsc && node build && mocha` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 206 | `mocha dist/test.js` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 205 | `npm run compile && mocha lib/spec/content && mocha lib/spec/core && mocha lib/spec/middleware && mocha lib/spec/tasks` | 
| [R-js/blasjs](https://github.com/R-js/blasjs) | 204 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 200 | `mocha -R spec test/integration` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 199 | `mocha js` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 197 | `nyc mocha --recursive test/**/*.ts` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 196 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [emmanueltouzery/prelude-ts](https://github.com/emmanueltouzery/prelude-ts) | 196 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 195 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 192 | `tsc && mocha` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 186 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 185 | `npm run build && npm run mocha` | 
| [woutervh-/typescript-is](https://github.com/woutervh-/typescript-is) | 180 | `npm run lint && npm run build && ttsc --project tsconfig-test.json && mocha` | 
| [nodejs/llhttp](https://github.com/nodejs/llhttp) | 177 | `npm run mocha && npm run lint` | 
| [Chinachu/Mirakurun](https://github.com/Chinachu/Mirakurun) | 176 | `mocha --exit test/*.spec.js` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 175 | `tsc && cd dist && mocha` | 
| [Microsoft/typescript-tslint-plugin](https://github.com/Microsoft/typescript-tslint-plugin) | 174 | `mocha ./out/**/*.test.js --slow 2000 --timeout 10000` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 174 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 173 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 172 | `npm run lint && npm run mocha` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 171 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [googleapis/nodejs-translate](https://github.com/googleapis/nodejs-translate) | 171 | `nyc mocha build/test` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 169 | `nyc --reporter=html --reporter=text mocha` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 163 | `gulp compile && mocha --timeout 10000 -u tdd ./out/tests/` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 163 | `npm run clean && npm run build && npm run lint && mocha` | 
| [p-society/typeracer-cli](https://github.com/p-society/typeracer-cli) | 162 | `mocha --no-deprecation --timeout 10000 --require ts-node/register **/*.spec.ts` | 
| [nomiclabs/buidler](https://github.com/nomiclabs/buidler) | 161 | `nyc mocha` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 161 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 160 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 159 | `gulp compile && mocha` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 159 | `npm run-script build && mocha --opts test/mocha.opts build/test/config.js build/test` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 158 | `mocha -r ts-node/register test/*.ts` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 156 | `mocha --require ts-node/register test/**/*.ts` | 
| [cartant/rxjs-marbles](https://github.com/cartant/rxjs-marbles) | 156 | `yarn run lint && yarn run test:build && cross-env FAILING=0 yarn run test:ava && cross-env FAILING=0 yarn run test:jasmine && cross-env FAILING=0 yarn run test:jasmine-angular && cross-env FAILING=0 yarn run test:jest && cross-env FAILING=0 yarn run test:mocha && cross-env FAILING=0 yarn run test:tape` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 154 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 152 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 150 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 149 | `mocha --require espower-typescript/guess "test/**/*.test.ts"` | 
| [arfedulov/semantic-ui-calendar-react](https://github.com/arfedulov/semantic-ui-calendar-react) | 148 | `npx cross-env TS_NODE_COMPILER_OPTIONS="{""allowJs"":true}" npx mocha -r ts-node/register ./test/setup.js ./test/**/*.{js,jsx,ts,tsx}` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 148 | `mocha lib/test` | 
| [Soluto/graphql-to-mongodb](https://github.com/Soluto/graphql-to-mongodb) | 145 | `ts-mocha tests/**/*.spec.ts` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 145 | `mocha` | 
| [TrustWallet/trust-ray](https://github.com/TrustWallet/trust-ray) | 144 | `cross-env NODE_ENV=test mocha --recursive --require ts-node/register 'test/**/*.test.ts' --exit` | 
| [DotJoshJohnson/vscode-xml](https://github.com/DotJoshJohnson/vscode-xml) | 143 | `npm run compile && mocha ./out/test/**/*.js` | 
| [calidion/vig](https://github.com/calidion/vig) | 143 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [vrimar/construct-ui](https://github.com/vrimar/construct-ui) | 142 | `cross-env TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 142 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 141 | `TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [featurist/hyperdom](https://github.com/featurist/hyperdom) | 141 | `./node_modules/.bin/tsc && npm run karma && npm run mocha && eslint . && npm run tslint` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 141 | `mocha` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 140 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 138 | `mocha` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 137 | `mocha test/unit/ --exit` | 
| [Azure/azure-functions-pack](https://github.com/Azure/azure-functions-pack) | 137 | `npm run build && mocha --compilers ts:ts-node/register --recursive test/**/*-spec.ts` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 137 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 135 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 134 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 134 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [colyseus/colyseus.js](https://github.com/colyseus/colyseus.js) | 134 | `mocha test/*.ts --require ts-node/register` | 
| [rtfeldman/node-elm-compiler](https://github.com/rtfeldman/node-elm-compiler) | 133 | `rm -rf test/fixtures/elm-stuff && mocha test/**/*.ts --require ts-node/register --watch-extensions ts` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 131 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 130 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 130 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 130 | `TEST_BROWSER_DRIVER=puppeteer meteor test --driver-package=ardatan:mocha --raw-logs` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 129 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 129 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 128 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 127 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 127 | `cross-env NODE_ENV=test mocha --exit` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 127 | `mocha --full-trace tests/test.js  --reporter mocha-multi-reporters` | 
| [prh/prh](https://github.com/prh/prh) | 127 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 127 | `mocha test` | 
| [Esri/react-arcgis](https://github.com/Esri/react-arcgis) | 126 | `nyc mocha` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 126 | `mocha --require source-map-support/register dist/test` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 126 | `mocha --timeout 10000` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 125 | `istanbul test -- _mocha` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 124 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 124 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 122 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 122 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 122 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 121 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 120 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 118 | `mocha --require ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [googleapis/nodejs-pubsub](https://github.com/googleapis/nodejs-pubsub) | 118 | `nyc mocha build/test` | 
| [bpatrik/pigallery2](https://github.com/bpatrik/pigallery2) | 115 | `ng test && mocha --recursive test/backend/unit && mocha --recursive test/backend/integration  && mocha --recursive test/common/unit ` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 114 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 114 | `mocha --recursive -t 4000` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 113 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 113 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 112 | `nyc npm run _mocha` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 112 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 111 | `npm run lint && npm run prettier && npm run mocha` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 111 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 110 | `nyc mocha --config ./test/.mocharc.yml` | 
| [nodejs/llparse](https://github.com/nodejs/llparse) | 110 | `npm run mocha && npm run lint` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 109 | `npm-run-all build test:mocha test:coverage lint` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 109 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 109 | `webpack && mocha-phantomjs test/index.html` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 108 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [ChainSafeSystems/lodestar](https://github.com/ChainSafeSystems/lodestar) | 107 | `nyc -r lcov -e .ts -x "*.test.ts" mocha -r ./.babel-register "tests/**/*.test.ts" && nyc report` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 107 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 106 | `mocha -R spec dist/test/**/*.js --exit` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 105 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 105 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [wildbit/postmark.js](https://github.com/wildbit/postmark.js) | 105 | `node_modules/mocha/bin/mocha --timeout 10000 --retries 1 -r ts-node/register test/**/*test.ts` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 104 | `mocha` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 104 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 104 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 103 | `mocha ./spec/*.js` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 103 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 101 | `tsc; mocha --recursive lib/ test/runner` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 101 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 101 | `mocha test/* --timeout 500000` | 
| [giantmachines/redux-websocket](https://github.com/giantmachines/redux-websocket) | 100 | `mocha --compilers js:babel-core/register` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 100 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 100 | `mocha --ui tdd out/test/extension.test.js` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 100 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [levjj/esverify](https://github.com/levjj/esverify) | 99 | `TS_NODE_TRANSPILE_ONLY=true mocha -r ts-node/register tests/*.ts` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 98 | `mocha -r ./src/test/common/setup.ts ./lib/src/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 98 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 97 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register/type-check 'test/**/*.ts'` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 97 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 97 | `node node_modules/mocha/bin/mocha` | 
| [mtmr0x/nucleo](https://github.com/mtmr0x/nucleo) | 95 | `mocha -r ts-node/register` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 94 | `nyc mocha build/test` | 
| [sunzongzheng/musicApi](https://github.com/sunzongzheng/musicApi) | 94 | `mocha -t 30000 --require @babel/register 'test/*.test.js' --exit` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 94 | `mocha` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 93 | `mocha ./dist/test --recursive` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 92 | `mocha test/ --recursive` | 
| [puzzle-js/puzzle-js](https://github.com/puzzle-js/puzzle-js) | 90 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 89 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 89 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 88 | `npm run lint && npm run mocha && npm run docs` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 88 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [roblox-ts/roblox-ts](https://github.com/roblox-ts/roblox-ts) | 88 | `npm run build && npx nyc --reporter=html mocha --timeout 0 --recursive out/test.js && lua tests/spec.lua` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 87 | `tsc && mocha "dist/test/**/*.js" ` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 87 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 87 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 86 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 86 | `mocha --require ts-node/register test/**/*.ts` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 86 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [googleapis/nodejs-datastore](https://github.com/googleapis/nodejs-datastore) | 85 | `nyc mocha build/test` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 84 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 84 | `mocha --timeout 10000 --slow 2500 tests/unittests/**/*.spec.js tests/functional-test-cases.js` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 83 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 83 | `mocha --compilers js:babel-core/register --recursive` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 81 | `mocha` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [teambition/ReactiveDB](https://github.com/teambition/ReactiveDB) | 80 | `npm run lint && NODE_ENV=test tman --mocha spec-js/test/run.js` | 
| [CityOfZion/neo-js](https://github.com/CityOfZion/neo-js) | 79 | `mocha --reporter spec` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 79 | `nyc mocha --require ts-node/register test/**/*Test.ts` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 79 | `mocha -r ts-node/register 'test/main.js'` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 79 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 79 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 78 | `mocha -u tdd ./out/tests/` | 
| [rpgeeganage/async-ray](https://github.com/rpgeeganage/async-ray) | 78 | `nyc mocha` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 78 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 77 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 77 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 77 | `TS_NODE_FILES=true mocha --opts src/test/mocha.opts "src/test/test*.ts"` | 
| [WorldBrain/storex](https://github.com/WorldBrain/storex) | 77 | `mocha --require ts-node/register "ts/**/*.test.ts"` | 
| [teamdomy/domy](https://github.com/teamdomy/domy) | 77 | `mocha --reporter spec --require ts-node/register 'tests/**/*.spec.ts'` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 76 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [balena-io/balena-supervisor](https://github.com/balena-io/balena-supervisor) | 76 | `npm run lint && npm run test:build && JUNIT_REPORT_PATH=report.xml istanbul cover _mocha && npm run coverage` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 76 | `npm run lint && nyc mocha` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 75 | `nyc mocha --recursive test/**/*.ts` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 75 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 75 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 74 | `yarn run lint && yarn run test:build && yarn run test:mocha` | 
| [ngduc/node-rem](https://github.com/ngduc/node-rem) | 74 | `cross-env NODE_ENV=test nyc --reporter=html --reporter=text --reporter=lcov mocha --require ts-node/register --full-trace --bail --timeout 20000 --exit tests/**/*.ts` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 74 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 73 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 73 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 73 | `npm run compile && mocha && npm run lint` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 73 | `mocha out/**/*.spec.js` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 73 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [WittBulter/koa2-typescript-guide](https://github.com/WittBulter/koa2-typescript-guide) | 72 | `mocha` | 
| [lukeautry/ts-app](https://github.com/lukeautry/ts-app) | 72 | `cross-env TS_NODE_PROJECT=./api/tsconfig.json mocha -t 15000 -r ts-node/register "./api/**/*.spec.ts"` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 72 | `mocha .tmp/spec/index.spec.js` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 71 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 71 | `nyc mocha` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 70 | `mocha` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 70 | `nyc mocha build/test` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 70 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 70 | `nyc mocha` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 69 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 69 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [Cellule/dndGenerator](https://github.com/Cellule/dndGenerator) | 69 | `mocha -r ./mocha-setup src/**/*.spec.ts` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 69 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 69 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 68 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [Alfresco/alfresco-js-api](https://github.com/Alfresco/alfresco-js-api) | 67 | `mocha --full-trace -r ts-node/register test/*.spec.ts test/**/*.spec.ts` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 67 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 67 | `mocha -r ts-node/register test/*.ts` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 66 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [mysticatea/regexpp](https://github.com/mysticatea/regexpp) | 66 | `nyc _mocha "test/*.ts" --reporter dot --timeout 10000` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 66 | `mocha build/tests/index.js` | 
| [angular-extensions/model](https://github.com/angular-extensions/model) | 66 | `npm run lint && npm run format:test && nyc mocha {lib,schematics}/**/*.test.ts --require ts-node/register --require source-map-support/register` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 66 | `mocha 'lib/**/__tests__/*.js'` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 66 | `mocha --timeout 99999999 --exit -r ts-node/register test/**/*.spec.ts` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 66 | `npm run clean && npm run build && mocha && npm run lint` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 65 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 65 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 64 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [demipixel/factorio-blueprint](https://github.com/demipixel/factorio-blueprint) | 64 | `mocha` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 64 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 64 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 63 | `node_modules/.bin/mocha --watch` | 
| [JustClear/colority](https://github.com/JustClear/colority) | 63 | `mocha test/index.js` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 63 | `mocha --opts test/mocha.opts` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 63 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [nhabuiduc/react-filter-box](https://github.com/nhabuiduc/react-filter-box) | 63 | `node --max-old-space-size=16000 ./node_modules/.bin/mocha-webpack --require ignore-styles -r jsdom-global/register --webpack-config webpack.test.config.js --watch "./test/**/*.ts"` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 63 | `mocha dist/test/*.js` | 
| [balmbees/dynamo-types](https://github.com/balmbees/dynamo-types) | 63 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 62 | `mocha out/test` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 62 | `nyc mocha` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 61 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 61 | `mocha test/*.js` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 61 | `tsc --version && tsc && mocha out/test` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 61 | `mocha --timeout 30000 test/**/*.js` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 61 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [wix/rawss](https://github.com/wix/rawss) | 60 | `mocha` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 60 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 60 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 59 | `npm run compile && mocha` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 59 | `mocha` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 59 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 59 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 59 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [mono/TsToCSharp](https://github.com/mono/TsToCSharp) | 59 | `npm run lint && mocha  ./dist/TsToCSharpTests.js` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 58 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 58 | `cross-env NODE_ENV=test mocha` | 
| [yesmeck/waque](https://github.com/yesmeck/waque) | 58 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 58 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 58 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 58 | `mocha` | 
| [hg-pyun/iterize](https://github.com/hg-pyun/iterize) | 58 | `mocha --recursive ./test/*.ts --require ts-node/register` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 56 | `mocha --ui qunit` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 56 | `mocha --recursive --reporter-options mochaFile=report.xml --reporter mocha-junit-reporter` | 
| [weaveworks/promjs](https://github.com/weaveworks/promjs) | 56 | `mocha --recursive "test/**/*-test.ts"` | 
| [strongloop/loopback4-example-shopping](https://github.com/strongloop/loopback4-example-shopping) | 55 | `lb-mocha --allow-console-logs "dist/test"` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 55 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 55 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 55 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 54 | `mocha --opts config/mocha.opts` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 54 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 54 | `npm run compile && mocha && npm run lint` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 54 | `npm run build && npm run mocha` | 
| [asakusuma/swae](https://github.com/asakusuma/swae) | 54 | `yarn build && rm -rf test/dist && yarn run lint && yarn run build-test && mocha test/dist/test/**/*.spec.js --timeout 15000` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 54 | `nyc mocha` | 
| [rpgeeganage/ifto](https://github.com/rpgeeganage/ifto) | 54 | `nyc mocha` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 54 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [desertkun/hiera-editor](https://github.com/desertkun/hiera-editor) | 54 | `mocha --timeout 15000 dist/tests/**/*.js` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 54 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 54 | `nyc mocha --opts test/mocha.opts` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 53 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 53 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [jackrobertscott/graphql-api-demo](https://github.com/jackrobertscott/graphql-api-demo) | 53 | `NODE_ENV=test mocha --require=ts-node/register --recursive --exit 'src/**/*.spec.ts'` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 53 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 53 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [jackrobertscott/graphql-api-demo](https://github.com/jackrobertscott/graphql-api-demo) | 53 | `NODE_ENV=test mocha --require=ts-node/register --recursive --exit 'src/**/*.spec.ts'` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 53 | `cross-env TS_NODE_FILES=true nyc mocha test/**/*.ts` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 52 | `NODE_ENV=test nyc mocha` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 52 | `NODE_ENV=test nyc mocha` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 52 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 52 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 52 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 52 | `mocha` | 
| [voodooattack/serialism](https://github.com/voodooattack/serialism) | 52 | `nyc mocha --expose-gc --ui mocha-typescript test/test_**.ts` | 
| [VoxaAI/voxa](https://github.com/VoxaAI/voxa) | 52 | `mocha test/*.spec.* test/**/*.spec.*` | 
| [Microsoft/vscode-html-languageservice](https://github.com/Microsoft/vscode-html-languageservice) | 51 | `npm run compile && mocha && npm run lint` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 51 | `mocha --opts mocha.opts --watch` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 51 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 51 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 51 | `cross-env NODE_ENV=test mocha test/**/*.ts` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 51 | `mocha` | 
| [BeTomorrow/ReImproveJS](https://github.com/BeTomorrow/ReImproveJS) | 51 | `mocha --reporter spec --compilers ts:ts-node/register 'test/*.spec.ts' --timeout 120000` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [teppeis/closure-ts](https://github.com/teppeis/closure-ts) | 51 | `npm-run-all --aggregate-output -p lint:ts build -p lint:js mocha` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 50 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 50 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 49 | `mocha --compilers ts:ts-node/register --recursive` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 49 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [SPGoding/spu](https://github.com/SPGoding/spu) | 49 | `mocha --require espower-typescript/guess "./src/test/**/*.ts"` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 48 | `mocha --opts cli-test-mocha.opts` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 48 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 48 | `nyc mocha build/test` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 48 | `mocha --recursive` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 48 | `nyc mocha build/test` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 48 | `mocha --recursive` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [RobinCK/typeorm-fixtures](https://github.com/RobinCK/typeorm-fixtures) | 48 | `nyc mocha` | 
| [NativeScript/nativescript-dev-appium](https://github.com/NativeScript/nativescript-dev-appium) | 47 | `mocha --timeout 999999` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 47 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [ProjectOpenSea/opensea-js](https://github.com/ProjectOpenSea/opensea-js) | 46 | `./node_modules/.bin/mocha test/*.ts --require ts-node/register --timeout 15000` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 46 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 46 | `mocha` | 
| [Jiasm/typescript-example](https://github.com/Jiasm/typescript-example) | 46 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 46 | `mocha test` | 
| [Rich-Harris/yootils](https://github.com/Rich-Harris/yootils) | 46 | `mocha --opts mocha.opts` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 45 | `npm run lint && mocha dist/spec` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 45 | `mocha out/{,**/}*.spec.js -s 0` | 
| [ethereum-ts/evm-ts](https://github.com/ethereum-ts/evm-ts) | 45 | `yarn lint && yarn test:mocha` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 45 | `mocha && npm run aplus` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 45 | `mocha -R spec ./test` | 
| [olivierlsc/swagger-express-ts](https://github.com/olivierlsc/swagger-express-ts) | 45 | `echo "Testing..." && npm run build && nyc mocha` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 45 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 45 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 44 | `node_modules/.bin/mocha` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 44 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [sourcegraph/browser-extensions](https://github.com/sourcegraph/browser-extensions) | 44 | `mocha --require ts-node/register --watch --watch-extensions ts './src/**/*.test.ts?(x)'` | 
| [pokemongo-dev-contrib/pokemongo-json-pokedex](https://github.com/pokemongo-dev-contrib/pokemongo-json-pokedex) | 44 | `mocha --recursive --compilers ts:ts-node/register,ts:tsconfig-paths/register test/*.ts test/**/*.ts` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 44 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 44 | `atool-test-mocha ./src/**/*-test.js` | 
| [heremaps/harp.gl](https://github.com/heremaps/harp.gl) | 44 | `ts-mocha -r tsconfig-paths/register ./test/*.ts ./@here/*/test/*.ts` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 43 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [Pushwoosh/web-push-notifications](https://github.com/Pushwoosh/web-push-notifications) | 43 | `mocha` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 43 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [gcanti/hyper-ts](https://github.com/gcanti/hyper-ts) | 43 | `npm run prettier && npm run lint && npm run typings-checker && npm run mocha` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 43 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 43 | `tsc && mocha spec/` | 
| [FontoXML/fontoxpath](https://github.com/FontoXML/fontoxpath) | 43 | `ts-mocha --require test/testhook.js "test/specs/**/*.ts"` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 42 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 42 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [azu/localstorage-ponyfill](https://github.com/azu/localstorage-ponyfill) | 42 | `mocha "test/**/*.ts"` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 42 | `tsc && mocha build/test` | 
| [NEEOInc/neeo-sdk](https://github.com/NEEOInc/neeo-sdk) | 42 | `TS_NODE_PROJECT=./test/tsconfig.json nyc mocha ./test/**/*.ts --opts ./test/mocha.opts` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 41 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 41 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [shogogg/ts-option](https://github.com/shogogg/ts-option) | 41 | `mocha --reporter spec --compilers ts:espower-typescript/guess` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 41 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 41 | `mocha index.test.js` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 41 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [Webtomizer/typeorm-loader](https://github.com/Webtomizer/typeorm-loader) | 40 | `npm run build && [ -d tests ] && NODE_ENV=test mocha $NODE_DEBUG_OPTION -r ts-node/register -r tslib tests/test_**.ts` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 40 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 40 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 40 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 40 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 40 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [googleapis/github-repo-automation](https://github.com/googleapis/github-repo-automation) | 40 | `nyc mocha build/test` | 
| [lolamtisch/MALSync](https://github.com/lolamtisch/MALSync) | 40 | `webpack --config webpackConfig/test.config.js && mocha --recursive --timeout 30000 --retries 2 test/headless` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 40 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 40 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [bromne/typescript-optional](https://github.com/bromne/typescript-optional) | 40 | `nyc mocha src/*` | 
| [nicolaspanel/three-orbitcontrols-ts](https://github.com/nicolaspanel/three-orbitcontrols-ts) | 40 | `mocha --opts mocha.opts` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 39 | `tsc && npm run lint && mocha` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 39 | `mocha --opts ./mocha.opts` | 
| [konvajs/ng2-konva](https://github.com/konvajs/ng2-konva) | 39 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 