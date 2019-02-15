# Find Repos in TypeScript Tested using Mocha

The list was updated at 01:55:45 02/15/19 PST

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 69250 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 17061 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 12654 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 11091 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 7172 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 6494 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 5671 | `npm run mocha` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 4800 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4713 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4711 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [rrweb-io/rrweb](https://github.com/rrweb-io/rrweb) | 3852 | `npm run bundle:browser && cross-env TS_NODE_CACHE=false TS_NODE_FILES=true mocha -r ts-node/register test/**/*.test.ts` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3433 | `mocha --opts mocha.opts` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 3114 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2977 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2892 | `mocha` | 
| [electron-userland/electron-forge](https://github.com/electron-userland/electron-forge) | 2600 | `cross-env TS_NODE_FILES=true yarn run mocha './tools/test-globber.ts' --opts mocha.opts` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2447 | `mocha 'test/**/*.ts'` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2313 | `mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [benjamn/recast](https://github.com/benjamn/recast) | 2222 | `npm run tsc && npm run mocha` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1940 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1922 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1811 | `mocha` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1784 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [colyseus/colyseus](https://github.com/colyseus/colyseus) | 1530 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1474 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1461 | `nyc -x '' mocha` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 1443 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [shanalikhan/code-settings-sync](https://github.com/shanalikhan/code-settings-sync) | 1390 | `npm run tslint-check && tsc -p ./ && mocha --recursive "./out/test/**/*.js"` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1329 | `mocha --opts mocha.opts` | 
| [cherow/cherow](https://github.com/cherow/cherow) | 1290 | `cross-env TS_NODE_PROJECT="test/tsconfig.json" mocha "test/**/*.ts" -c -R progress -r ts-node/register -r source-map-support/register --recursive --globals expect` | 
| [google/clasp](https://github.com/google/clasp) | 1277 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [funkia/list](https://github.com/funkia/list) | 1246 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1243 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1228 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1158 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1112 | `nyc --reporter=html --reporter=text mocha` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 1088 | `tsc -p ./ && mocha` | 
| [itchio/itch](https://github.com/itchio/itch) | 1022 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 951 | `mocha --opts test/mocha.opts` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 941 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 936 | `mocha bin/tests/test.js` | 
| [stryker-mutator/stryker](https://github.com/stryker-mutator/stryker) | 856 | `npm run mocha` | 
| [NativeScript/nativescript-cli](https://github.com/NativeScript/nativescript-cli) | 805 | `istanbul cover ./node_modules/mocha/bin/_mocha` | 
| [netgusto/nodebook](https://github.com/netgusto/nodebook) | 782 | `mocha test/backend` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 781 | `mocha --require ts-node/register` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 744 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 739 | `yarn run lint && yarn run test:mocha` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 728 | `mocha` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 728 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 716 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 710 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 685 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 646 | `mocha --recursive` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 640 | `mocha "out/**/*.spec.js" -s 0` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 637 | `mocha test/unit` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 624 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 609 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [JustClear/blurify](https://github.com/JustClear/blurify) | 597 | `mocha test/index.js` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 596 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 596 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 594 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [googleapis/google-auth-library-nodejs](https://github.com/googleapis/google-auth-library-nodejs) | 593 | `nyc mocha build/test` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 593 | `npm run lint && npm run mocha` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 584 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 583 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [bbc/sqs-consumer](https://github.com/bbc/sqs-consumer) | 579 | `mocha` | 
| [dsherret/ts-morph](https://github.com/dsherret/ts-morph) | 567 | `cross-env TS_NODE_COMPILER="ttypescript" TS_NODE_TRANSPILE_ONLY="true" mocha --opts mocha.opts --grep @performance --invert` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 562 | `mocha` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 559 | `mocha test` | 
| [mateogianolio/vectorious](https://github.com/mateogianolio/vectorious) | 547 | `nyc mocha -r ts-node/register ./src/*.spec.ts` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 538 | `mocha --opts test/mocha.opts dist/test` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 529 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 511 | `cross-env NODE_ENV=tsoa_test mocha **/*.spec.ts --exit --compilers ts:ts-node/register` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 506 | `tsc && mocha test && yarn lint` | 
| [benjamn/ast-types](https://github.com/benjamn/ast-types) | 501 | `npm run gen && npm run build && npm run mocha` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 499 | `mocha --opts mocha.opts` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 493 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 492 | `mocha --opts mocha.opts` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 489 | `npm run mocha` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 489 | `cd test && mocha -r ts-node/register *.ts` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 487 | `npm run lint && npm run mocha` | 
| [Cookie-AutoDelete/Cookie-AutoDelete](https://github.com/Cookie-AutoDelete/Cookie-AutoDelete) | 483 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec ./test/*` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 467 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 461 | `npm run build && mocha` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 451 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 444 | `_mocha --` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 436 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 415 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 404 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 396 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 383 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [R-js/libRmath.js](https://github.com/R-js/libRmath.js) | 381 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [amplify-education/serverless-domain-manager](https://github.com/amplify-education/serverless-domain-manager) | 375 | `tsc --project . && nyc mocha -r ts-node/register test/unit-tests/index.test.ts && nyc report --reporter=text-summary` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 363 | `npm run build && mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 361 | `mocha` | 
| [Microsoft/node-pty](https://github.com/Microsoft/node-pty) | 360 | `cross-env NODE_ENV=test mocha -R spec --exit lib/*.test.js` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 358 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 352 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 350 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 347 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 333 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 331 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts extension/test/test-*.ts view/test/test-heightmap.ts` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 329 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 322 | `mocha` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 318 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 317 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 310 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 298 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 294 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 292 | `mocha` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 292 | `mocha lib/test` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 288 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec --bail` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 279 | `mocha` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 279 | `mocha --compilers js:babel-register test/**/*.js` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 273 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 269 | `mocha-webpack "src/**/*.ts"` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 268 | `mocha src/**/*.spec.ts` | 
| [juanfranblanco/vscode-solidity](https://github.com/juanfranblanco/vscode-solidity) | 268 | `nyc --require ts-node/register --require source-map-support/register mocha test/**/*.spec.ts` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 264 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 264 | `mocha "test/**/*.spec.ts"` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 263 | `tsc && mocha dist/**/*.spec.js` | 
| [nwtgck/piping-server](https://github.com/nwtgck/piping-server) | 258 | `mocha --require ts-node/register --timeout 10000 test/**/*.ts` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 255 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [slothking-online/diagram](https://github.com/slothking-online/diagram) | 255 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 251 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 251 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [AmirTugi/tea-school](https://github.com/AmirTugi/tea-school) | 249 | `npx ts-mocha ./src/tests/**.ts` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 245 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 239 | `cd test && mocha -r ts-node/register *.ts` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 238 | `tsc && mocha` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 238 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | 231 | `nyc mocha` | 
| [googleapis/nodejs-storage](https://github.com/googleapis/nodejs-storage) | 230 | `nyc mocha build/test` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 229 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 226 | `nyc --reporter html mocha` | 
| [Odi-ts/odi](https://github.com/Odi-ts/odi) | 226 | `nyc mocha test/**/*.test.ts --exit` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 218 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 218 | `cross-env NODE_ENV=test mocha --exit` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 216 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 209 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 209 | `mocha test` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 207 | `mocha dist/test.js` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 206 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [bmewburn/intelephense](https://github.com/bmewburn/intelephense) | 206 | `mocha -r ts-node/register test/*.ts` | 
| [Zarel/Pokemon-Showdown-Client](https://github.com/Zarel/Pokemon-Showdown-Client) | 204 | `eslint --config=.eslintrc.js --cache --cache-file=eslint-cache/base js/ data/ && eslint --config=build-tools/.eslintrc.js --cache --cache-file=eslint-cache/build build-tools/update build-tools/build-indexes && tslint --project . && tsc && node build && mocha` | 
| [R-js/blasjs](https://github.com/R-js/blasjs) | 202 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 200 | `mocha -R spec test/integration` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 197 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 195 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 195 | `mocha lib/spec/core` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 192 | `mocha js` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 189 | `nyc mocha --recursive test/**/*.ts` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 186 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 185 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [emmanueltouzery/prelude-ts](https://github.com/emmanueltouzery/prelude-ts) | 181 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 179 | `npm run build && npm run mocha` | 
| [nodejs/llhttp](https://github.com/nodejs/llhttp) | 173 | `npm run mocha && npm run lint` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 173 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 173 | `tsc && cd dist && mocha` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 172 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 172 | `npm run lint && npm run mocha` | 
| [Chinachu/Mirakurun](https://github.com/Chinachu/Mirakurun) | 169 | `mocha --exit test/*.spec.js` | 
| [PeterDing/chord](https://github.com/PeterDing/chord) | 166 | `./node_modules/mocha/bin/mocha --delay` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 165 | `npm run clean && npm run build && npm run lint && mocha` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 162 | `gulp compile && mocha --timeout 10000 -u tdd ./out/tests/` | 
| [googleapis/nodejs-translate](https://github.com/googleapis/nodejs-translate) | 162 | `nyc mocha build/test` | 
| [p-society/typeracer-cli](https://github.com/p-society/typeracer-cli) | 159 | `mocha --no-deprecation --timeout 10000 --require ts-node/register **/*.spec.ts` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 157 | `gulp compile && mocha` | 
| [Microsoft/typescript-tslint-plugin](https://github.com/Microsoft/typescript-tslint-plugin) | 156 | `mocha ./out/**/*.test.js --slow 2000 --timeout 10000` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 156 | `tsc && mocha` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 156 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 155 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 154 | `nyc --reporter=html --reporter=text mocha` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 153 | `mocha --require ts-node/register test/**/*.ts` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 153 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 152 | `mocha -r ts-node/register test/*.ts` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 151 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 151 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [cartant/rxjs-marbles](https://github.com/cartant/rxjs-marbles) | 147 | `yarn run lint && yarn run test:build && cross-env FAILING=0 yarn run test:ava && cross-env FAILING=0 yarn run test:jasmine && cross-env FAILING=0 yarn run test:jasmine-angular && cross-env FAILING=0 yarn run test:jest && cross-env FAILING=0 yarn run test:mocha && cross-env FAILING=0 yarn run test:tape` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 146 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 145 | `npm run-script build && mocha --opts test/mocha.opts build/test/config.js build/test` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 145 | `mocha lib/test` | 
| [woutervh-/typescript-is](https://github.com/woutervh-/typescript-is) | 144 | `npm run lint && npm run build && ttsc --project tsconfig-test.json && mocha` | 
| [calidion/vig](https://github.com/calidion/vig) | 144 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 141 | `mocha --require espower-typescript/guess "test/**/*.test.ts"` | 
| [featurist/hyperdom](https://github.com/featurist/hyperdom) | 139 | `./node_modules/.bin/tsc && npm run karma && npm run mocha && eslint . && npm run tslint` | 
| [DotJoshJohnson/vscode-xml](https://github.com/DotJoshJohnson/vscode-xml) | 138 | `npm run compile && mocha ./out/test/**/*.js` | 
| [nomiclabs/buidler](https://github.com/nomiclabs/buidler) | 138 | `nyc mocha` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 138 | `mocha` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 138 | `mocha` | 
| [vrimar/construct-ui](https://github.com/vrimar/construct-ui) | 137 | `cross-env TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [TrustWallet/trust-ray](https://github.com/TrustWallet/trust-ray) | 137 | `cross-env NODE_ENV=test mocha --recursive --require ts-node/register 'test/**/*.test.ts' --exit` | 
| [Azure/azure-functions-pack](https://github.com/Azure/azure-functions-pack) | 137 | `npm run build && mocha --compilers ts:ts-node/register --recursive test/**/*-spec.ts` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 136 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 134 | `mocha test/unit/ --exit` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 133 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [Soluto/graphql-to-mongodb](https://github.com/Soluto/graphql-to-mongodb) | 133 | `ts-mocha tests/**/*.spec.ts` | 
| [colyseus/colyseus.js](https://github.com/colyseus/colyseus.js) | 132 | `mocha test/*.ts --require ts-node/register` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 131 | `npm run lint && node_modules/.bin/nyc --require source-map-support/register npm run mocha` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 131 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 131 | `TEST_BROWSER_DRIVER=puppeteer meteor test --driver-package=ardatan:mocha --raw-logs` | 
| [rtfeldman/node-elm-compiler](https://github.com/rtfeldman/node-elm-compiler) | 131 | `rm -rf test/fixtures/elm-stuff && mocha test/**/*.ts --require ts-node/register --watch-extensions ts` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 130 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 130 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [arfedulov/semantic-ui-calendar-react](https://github.com/arfedulov/semantic-ui-calendar-react) | 129 | `npx cross-env TS_NODE_COMPILER_OPTIONS="{""allowJs"":true}" npx mocha -r ts-node/register ./test/setup.js ./test/**/*.{js,jsx,ts,tsx}` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 128 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 128 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 127 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 127 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 125 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [prh/prh](https://github.com/prh/prh) | 125 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 125 | `mocha --require source-map-support/register dist/test` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 124 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 124 | `istanbul test -- _mocha` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 124 | `mocha test` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 124 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 124 | `mocha` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 124 | `mocha --timeout 10000` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 123 | `cross-env NODE_ENV=test mocha --exit` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 123 | `TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 123 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 121 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 120 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 120 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 119 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 116 | `mocha --full-trace tests/test.js  --reporter mocha-multi-reporters` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 113 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [Esri/react-arcgis](https://github.com/Esri/react-arcgis) | 113 | `nyc mocha` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 113 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 111 | `mocha --recursive -t 4000` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 110 | `mocha --require ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 110 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 110 | `webpack && mocha-phantomjs test/index.html` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 108 | `npm-run-all build test:mocha test:coverage lint` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 108 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 108 | `nyc npm run _mocha` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 107 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 107 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 107 | `mocha -R spec dist/test/**/*.js` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 107 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 105 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [nodejs/llparse](https://github.com/nodejs/llparse) | 105 | `npm run mocha && npm run lint` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 104 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 104 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 104 | `npm run lint && npm run prettier && npm run mocha` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 104 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 104 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [googleapis/nodejs-pubsub](https://github.com/googleapis/nodejs-pubsub) | 104 | `nyc mocha build/test` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 104 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 103 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [wildbit/postmark.js](https://github.com/wildbit/postmark.js) | 103 | `node_modules/mocha/bin/mocha --timeout 10000 --retries 1 -r ts-node/register test/**/*test.ts` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 102 | `mocha` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 102 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 100 | `tsc; mocha --recursive lib/ test/runner` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 100 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [bpatrik/pigallery2](https://github.com/bpatrik/pigallery2) | 99 | `ng test && mocha --recursive test/backend/unit && mocha --recursive test/backend/integration  && mocha --recursive test/common/unit ` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 99 | `mocha ./spec/*.js` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 98 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 98 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 97 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register/type-check 'test/**/*.ts'` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 97 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 97 | `mocha test/* --timeout 500000` | 
| [nucleojs/nucleo](https://github.com/nucleojs/nucleo) | 95 | `mocha -r ts-node/register` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 95 | `node node_modules/mocha/bin/mocha` | 
| [levjj/esverify](https://github.com/levjj/esverify) | 95 | `TS_NODE_TRANSPILE_ONLY=true mocha -r ts-node/register tests/*.ts` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 94 | `mocha ./dist/test --recursive` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 94 | `nyc mocha` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 93 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 93 | `mocha --ui tdd out/test/extension.test.js` | 
| [giantmachines/redux-websocket](https://github.com/giantmachines/redux-websocket) | 92 | `mocha --compilers js:babel-core/register` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 92 | `mocha test/ --recursive` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 92 | `mocha` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 90 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 89 | `nyc mocha build/test` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 89 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 88 | `mocha -r ./src/test/common/setup.ts ./lib/src/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 88 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [sunzongzheng/musicApi](https://github.com/sunzongzheng/musicApi) | 88 | `mocha -t 30000 --require @babel/register 'test/*.test.js' --exit` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 86 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 85 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 84 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 84 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 83 | `tsc && mocha "dist/test/**/*.js" ` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 83 | `mocha --compilers js:babel-core/register --recursive` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 83 | `mocha --require ts-node/register test/**/*.ts` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 81 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 81 | `mocha` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 80 | `npm run lint && npm run mocha` | 
| [googleapis/nodejs-datastore](https://github.com/googleapis/nodejs-datastore) | 80 | `nyc mocha build/test` | 
| [teambition/ReactiveDB](https://github.com/teambition/ReactiveDB) | 78 | `npm run lint && NODE_ENV=test tman --mocha spec-js/test/run.js` | 
| [rpgeeganage/async-ray](https://github.com/rpgeeganage/async-ray) | 78 | `nyc mocha` | 
| [CityOfZion/neo-js](https://github.com/CityOfZion/neo-js) | 78 | `mocha --reporter spec` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 78 | `mocha --timeout 10000 --slow 2500 tests/unittests/**/*.spec.js tests/functional-test-cases.js` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 77 | `mocha -u tdd ./out/tests/` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 77 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 77 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 77 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 77 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [roblox-ts/roblox-ts](https://github.com/roblox-ts/roblox-ts) | 77 | `npm run build && npx nyc --reporter=html mocha --timeout 0 --recursive out/test.js && lua tests/spec.lua` | 
| [balena-io/balena-supervisor](https://github.com/balena-io/balena-supervisor) | 76 | `npm run lint && npm run test:build && JUNIT_REPORT_PATH=report.xml istanbul cover _mocha && npm run coverage` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 76 | `npm run lint && nyc mocha` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 76 | `mocha -r ts-node/register 'test/main.js'` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 76 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 75 | `nyc mocha --recursive test/**/*.ts` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 75 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 75 | `nyc mocha lib/**/*Test.js` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 74 | `TS_NODE_FILES=true mocha --opts src/test/mocha.opts "src/test/test*.ts"` | 
| [teamdomy/domy](https://github.com/teamdomy/domy) | 74 | `mocha --reporter spec --require ts-node/register 'tests/**/*.spec.ts'` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 73 | `mocha out/**/*.spec.js` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 73 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 72 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 72 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 72 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 71 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 71 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 71 | `yarn run lint && yarn run test:build && yarn run test:mocha` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 71 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 71 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 71 | `yarn run lint && yarn run test:build && yarn run test:mocha` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 71 | `npm run compile && mocha && npm run lint` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 70 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [puzzle-js/puzzle-js](https://github.com/puzzle-js/puzzle-js) | 69 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 69 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 68 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 68 | `mocha .tmp/spec/index.spec.js` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 68 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd ./out/test/extension.test.js` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 67 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 67 | `mocha -r ts-node/register test/*.ts` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 66 | `nyc mocha build/test` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 66 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 65 | `nyc mocha --opts .mocha.opts` | 
| [Alfresco/alfresco-js-api](https://github.com/Alfresco/alfresco-js-api) | 65 | `mocha --full-trace -r ts-node/register test/*.spec.ts test/**/*.spec.ts` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 64 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [Cellule/dndGenerator](https://github.com/Cellule/dndGenerator) | 64 | `mocha -r ./mocha-setup src/**/*.spec.ts` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 64 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 64 | `nyc mocha` | 
| [lukeautry/ts-app](https://github.com/lukeautry/ts-app) | 63 | `cross-env TS_NODE_PROJECT=./api/tsconfig.json mocha -t 15000 -r ts-node/register "./api/**/*.spec.ts"` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 63 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 63 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 63 | `mocha 'lib/**/__tests__/*.js'` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 62 | `mocha` | 
| [DhyanaChina/koa2-typescript-guide](https://github.com/DhyanaChina/koa2-typescript-guide) | 62 | `mocha` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 62 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [JustClear/colority](https://github.com/JustClear/colority) | 62 | `mocha test/index.js` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 62 | `mocha build/tests/index.js` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 62 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 62 | `mocha dist/test/*.js` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 61 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 61 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 60 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [wix/rawss](https://github.com/wix/rawss) | 60 | `mocha` | 
| [nhabuiduc/react-filter-box](https://github.com/nhabuiduc/react-filter-box) | 60 | `node --max-old-space-size=16000 ./node_modules/.bin/mocha-webpack --require ignore-styles -r jsdom-global/register --webpack-config webpack.test.config.js --watch "./test/**/*.ts"` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 59 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 58 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 58 | `node_modules/.bin/mocha --watch` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 58 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 58 | `mocha --opts test/mocha.opts` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 58 | `mocha --timeout 30000 test/**/*.js` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 58 | `mocha out/test` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 57 | `npm run compile && mocha` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 57 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 57 | `mocha` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 57 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 57 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [mono/TsToCSharp](https://github.com/mono/TsToCSharp) | 57 | `npm run lint && mocha  ./dist/TsToCSharpTests.js` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 56 | `mocha test/*.js` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 56 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 56 | `nyc mocha` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 56 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [balmbees/dynamo-types](https://github.com/balmbees/dynamo-types) | 56 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 55 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 55 | `cross-env NODE_ENV=test mocha` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 55 | `tsc --version && tsc && mocha out/test` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 55 | `mocha --recursive --reporter-options mochaFile=report.xml --reporter mocha-junit-reporter` | 
| [hg-pyun/iterize](https://github.com/hg-pyun/iterize) | 55 | `mocha --recursive ./test/*.ts --require ts-node/register` | 
| [angular-extensions/model](https://github.com/angular-extensions/model) | 55 | `npm run lint && npm run format:test && nyc mocha {lib,schematics}/**/*.test.ts --require ts-node/register --require source-map-support/register` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 55 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 54 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 54 | `mocha` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 54 | `npm run build && npm run mocha` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 54 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [asakusuma/swae](https://github.com/asakusuma/swae) | 54 | `yarn build && rm -rf test/dist && yarn run lint && yarn run build-test && mocha test/dist/test/**/*.spec.js --timeout 15000` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 53 | `mocha --ui qunit` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 53 | `mocha --opts config/mocha.opts` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 53 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 53 | `mocha` | 
| [rpgeeganage/ifto](https://github.com/rpgeeganage/ifto) | 53 | `nyc mocha` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 53 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 53 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 52 | `NODE_ENV=test nyc mocha` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 52 | `npm run compile && mocha && npm run lint` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 52 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 52 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 52 | `nyc mocha` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 52 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 52 | `mocha --timeout 99999999 --exit -r ts-node/register test/**/*.spec.ts` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 52 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [yesmeck/waque](https://github.com/yesmeck/waque) | 51 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 51 | `NODE_ENV=test nyc mocha` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 51 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [aykutkardas/Json-Function](https://github.com/aykutkardas/Json-Function) | 51 | `cross-env TS_NODE_COMPILER_OPTIONS='{ "module": "commonjs" }' mocha -r ts-node/register -r ignore-styles -r jsdom-global/register test/**/*.spec.ts` | 
| [VoxaAI/voxa](https://github.com/VoxaAI/voxa) | 51 | `mocha test/*.spec.* test/**/*.spec.*` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 51 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [DhyanaChina/todo-live](https://github.com/DhyanaChina/todo-live) | 51 | `mocha` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 50 | `mocha --opts mocha.opts --watch` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 50 | `cross-env NODE_ENV=test mocha test/**/*.ts` | 
| [voodooattack/serialism](https://github.com/voodooattack/serialism) | 50 | `nyc mocha --expose-gc --ui mocha-typescript test/test_**.ts` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 50 | `nyc mocha --opts test/mocha.opts` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 49 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 49 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 49 | `mocha --compilers ts:ts-node/register --recursive` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 49 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [Grademark/grademark](https://github.com/Grademark/grademark) | 49 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [SPGoding/spu](https://github.com/SPGoding/spu) | 49 | `mocha --require espower-typescript/guess "./src/test/**/*.ts"` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 49 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [teppeis/closure-ts](https://github.com/teppeis/closure-ts) | 49 | `npm-run-all --aggregate-output -p lint:ts build -p lint:js mocha` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 48 | `mocha --require ts-node/register tests/**/*.ts` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 48 | `mocha --require ts-node/register tests/**/*.ts` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 48 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 48 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 48 | `nyc mocha --require source-map-support/register --require ts-node/register test/**/*.ts` | 
| [BeTomorrow/ReImproveJS](https://github.com/BeTomorrow/ReImproveJS) | 47 | `mocha --reporter spec --compilers ts:ts-node/register 'test/*.spec.ts' --timeout 120000` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 46 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 46 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [NativeScript/nativescript-dev-appium](https://github.com/NativeScript/nativescript-dev-appium) | 46 | `mocha --timeout 999999` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 46 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [desertkun/hiera-editor](https://github.com/desertkun/hiera-editor) | 46 | `mocha --timeout 15000 dist/tests/**/*.js` | 
| [jackrobertscott/graphql-api-demo](https://github.com/jackrobertscott/graphql-api-demo) | 46 | `NODE_ENV=test mocha --require=ts-node/register --recursive --exit 'src/**/*.spec.ts'` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 45 | `mocha --opts cli-test-mocha.opts` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 45 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 45 | `nyc mocha build/test` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 45 | `mocha` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 45 | `mocha -R spec ./test` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 45 | `mocha test` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 45 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 44 | `npm run lint && mocha dist/spec` | 
| [strongloop/loopback4-example-shopping](https://github.com/strongloop/loopback4-example-shopping) | 44 | `lb-mocha --allow-console-logs "dist/test"` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 44 | `mocha out/{,**/}*.spec.js -s 0` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 44 | `mocha --recursive` | 
| [ethereum-ts/evm-ts](https://github.com/ethereum-ts/evm-ts) | 44 | `yarn lint && yarn test:mocha` | 
| [sourcegraph/browser-extensions](https://github.com/sourcegraph/browser-extensions) | 44 | `mocha --require ts-node/register --watch --watch-extensions ts './src/**/*.test.ts?(x)'` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 44 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 44 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 43 | `node_modules/.bin/mocha` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 43 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 43 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [pokemongo-dev-contrib/pokemongo-json-pokedex](https://github.com/pokemongo-dev-contrib/pokemongo-json-pokedex) | 43 | `mocha --recursive --compilers ts:ts-node/register,ts:tsconfig-paths/register test/*.ts test/**/*.ts` | 
| [Pushwoosh/web-push-notifications](https://github.com/Pushwoosh/web-push-notifications) | 43 | `mocha` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 43 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 43 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 42 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 42 | `mocha && npm run aplus` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 42 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 42 | `atool-test-mocha ./src/**/*-test.js` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 42 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 42 | `tsc && mocha build/test` | 
| [NEEOInc/neeo-sdk](https://github.com/NEEOInc/neeo-sdk) | 42 | `TS_NODE_PROJECT=./test/tsconfig.json nyc mocha ./test/**/*.ts --opts ./test/mocha.opts` | 
| [ProjectOpenSea/opensea-js](https://github.com/ProjectOpenSea/opensea-js) | 41 | `./node_modules/.bin/mocha test/*.ts --require ts-node/register --timeout 15000` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 41 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [Jiasm/typescript-example](https://github.com/Jiasm/typescript-example) | 41 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 41 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [olivierlsc/swagger-express-ts](https://github.com/olivierlsc/swagger-express-ts) | 41 | `echo "Testing..." && npm run build && nyc mocha` | 
| [eclipse/sprotty](https://github.com/eclipse/sprotty) | 41 | `jenkins-mocha --opts ./configs/mocha.opts "./src/**/*.spec.?(ts|tsx)"` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 41 | `mocha index.test.js` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 41 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 41 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 41 | `tsc && mocha spec/` | 
| [FontoXML/fontoxpath](https://github.com/FontoXML/fontoxpath) | 41 | `ts-mocha --require test/testhook.js "test/specs/**/*.ts"` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 40 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [webix-hub/webix-jet](https://github.com/webix-hub/webix-jet) | 40 | `webpack && phantomjs node_modules/mocha-phantomjs-core/mocha-phantomjs-core.js tests/index.html spec` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 40 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 39 | `mocha --opts ./mocha.opts` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 39 | `tsc && npm run lint && mocha` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 39 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 39 | `mocha` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 39 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [josephg/statecraft](https://github.com/josephg/statecraft) | 39 | `mocha -r ts-node/register test/*.ts` | 
| [shogogg/ts-option](https://github.com/shogogg/ts-option) | 39 | `mocha --reporter spec --compilers ts:espower-typescript/guess` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 39 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [azu/localstorage-ponyfill](https://github.com/azu/localstorage-ponyfill) | 39 | `mocha "test/**/*.ts"` | 
| [gcanti/hyper-ts](https://github.com/gcanti/hyper-ts) | 39 | `npm run prettier && npm run lint && npm run typings-checker && npm run mocha` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 39 | `npm run mocha && npm run lint` | 
| [aurelia/bundler](https://github.com/aurelia/bundler) | 39 | `mocha --reporter spec --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 39 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 38 | `tsc && mocha dist/**/*.spec.js` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 38 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 38 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [RocketChat/Rocket.Chat.js.SDK](https://github.com/RocketChat/Rocket.Chat.js.SDK) | 38 | `nyc mocha './src/lib/**/*.spec.ts'` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 38 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 38 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [Webtomizer/typeorm-loader](https://github.com/Webtomizer/typeorm-loader) | 37 | `npm run build && [ -d tests ] && NODE_ENV=test mocha $NODE_DEBUG_OPTION -r ts-node/register -r tslib tests/test_**.ts` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 37 | `mocha test/*.spec.ts` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 37 | `mocha --recursive "dist/**/*.test.js"` | 
| [bromne/typescript-optional](https://github.com/bromne/typescript-optional) | 37 | `nyc mocha src/*` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 36 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 36 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 36 | `tsc -p .tsconfig.test.json && mocha` | 
| [paralin/grpc-bus](https://github.com/paralin/grpc-bus) | 36 | `npm run lint && npm run mocha` | 
| [ste-vg/pop.svg](https://github.com/ste-vg/pop.svg) | 36 | `nyc mocha --require ./mocha.config.js -r ts-node/register 'src/**/*.spec.ts'  --exit --recursive --timeout 10000` | 
| [infinum/mobx-collection-store](https://github.com/infinum/mobx-collection-store) | 36 | `NODE_ENV=test nyc mocha` | 