# Find Repos in TypeScript Tested using Mocha

The list was updated at 01:55:48 01/11/19 PST

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 67109 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 16608 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 11584 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 10272 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 7037 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 6290 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 5495 | `npm run mocha` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4648 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4527 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 4044 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3403 | `mocha --opts mocha.opts` | 
| [rrweb-io/rrweb](https://github.com/rrweb-io/rrweb) | 3188 | `npm run bundle:browser && cross-env TS_NODE_CACHE=false TS_NODE_FILES=true mocha -r ts-node/register test/**/*.test.ts` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 2919 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2862 | `mocha` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2837 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [electron-userland/electron-forge](https://github.com/electron-userland/electron-forge) | 2474 | `cross-env TS_NODE_FILES=true yarn run mocha './tools/test-globber.ts' --opts mocha.opts` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2437 | `mocha 'test/**/*.ts'` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2243 | `mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [benjamn/recast](https://github.com/benjamn/recast) | 2169 | `npm run tsc && npm run mocha` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1888 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1882 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1806 | `mocha` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1763 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1438 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1415 | `nyc -x '' mocha` | 
| [colyseus/colyseus](https://github.com/colyseus/colyseus) | 1404 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 1323 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [shanalikhan/code-settings-sync](https://github.com/shanalikhan/code-settings-sync) | 1286 | `npm run tslint-check && tsc -p ./ && mocha --recursive "./out/test/**/*.js"` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1273 | `mocha --opts mocha.opts` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1233 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [cherow/cherow](https://github.com/cherow/cherow) | 1228 | `cross-env TS_NODE_PROJECT="test/tsconfig.json" mocha "test/**/*.ts" -c -R progress -r ts-node/register -r source-map-support/register --recursive --globals expect` | 
| [funkia/list](https://github.com/funkia/list) | 1227 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1208 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [google/clasp](https://github.com/google/clasp) | 1144 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1128 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1102 | `nyc --reporter=html --reporter=text mocha` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 1057 | `tsc -p ./ && mocha` | 
| [itchio/itch](https://github.com/itchio/itch) | 1002 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 940 | `mocha --opts test/mocha.opts` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 926 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 891 | `mocha bin/tests/test.js` | 
| [netgusto/nodebook](https://github.com/netgusto/nodebook) | 770 | `mocha test/backend` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 754 | `mocha --require ts-node/register` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 735 | `yarn run lint && yarn run test:mocha` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 717 | `mocha` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 711 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 711 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 698 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 686 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 668 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 648 | `mocha --recursive` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 611 | `mocha "out/**/*.spec.js" -s 0` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 610 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 604 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [JustClear/blurify](https://github.com/JustClear/blurify) | 597 | `mocha test/index.js` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 593 | `npm run lint && npm run mocha` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 576 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 573 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 570 | `mocha test/unit` | 
| [googleapis/google-auth-library-nodejs](https://github.com/googleapis/google-auth-library-nodejs) | 567 | `nyc mocha build/test` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 561 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 555 | `mocha test` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 553 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 552 | `mocha` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 538 | `mocha --opts test/mocha.opts dist/test` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 530 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 528 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [dsherret/ts-simple-ast](https://github.com/dsherret/ts-simple-ast) | 514 | `cross-env TS_NODE_COMPILER="ttypescript" TS_NODE_TRANSPILE_ONLY="true" mocha --opts mocha.opts --grep @performance --invert` | 
| [benjamn/ast-types](https://github.com/benjamn/ast-types) | 494 | `npm run gen && npm run tsc && npm run mocha` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 488 | `mocha --opts mocha.opts` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 483 | `cross-env NODE_ENV=tsoa_test mocha **/*.spec.ts --exit --compilers ts:ts-node/register` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 481 | `mocha --opts mocha.opts` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 471 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 468 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 462 | `npm run build && mocha` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 459 | `npm run mocha` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 455 | `cd test && mocha -r ts-node/register *.ts` | 
| [Cookie-AutoDelete/Cookie-AutoDelete](https://github.com/Cookie-AutoDelete/Cookie-AutoDelete) | 453 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec ./test/*` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 453 | `tsc && mocha test && yarn lint` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 451 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 445 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 444 | `_mocha --` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 420 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 407 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 397 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 392 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 383 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [R-js/libRmath.js](https://github.com/R-js/libRmath.js) | 379 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 360 | `mocha` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 355 | `npm run build && mocha` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 349 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 340 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 338 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 328 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 318 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 309 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 307 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 300 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts view/test/test-heightmap.ts` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 299 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 299 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 298 | `mocha` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 293 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 291 | `mocha` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 288 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 287 | `mocha lib/test` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 279 | `mocha --compilers js:babel-register test/**/*.js` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 275 | `mocha` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 270 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 263 | `mocha src/**/*.spec.ts` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 251 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 251 | `mocha "test/**/*.spec.ts"` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 247 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 246 | `tsc && mocha dist/**/*.spec.js` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 245 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [AmirTugi/tea-school](https://github.com/AmirTugi/tea-school) | 242 | `npx ts-mocha ./src/tests/**.ts` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 242 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 240 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 237 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 226 | `nyc --reporter html mocha` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 223 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 222 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 215 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 211 | `mocha test` | 
| [googleapis/nodejs-storage](https://github.com/googleapis/nodejs-storage) | 210 | `nyc mocha build/test` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 206 | `mocha dist/test.js` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 211 | `mocha test` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 210 | `cd test && mocha -r ts-node/register *.ts` | 
| [googleapis/nodejs-storage](https://github.com/googleapis/nodejs-storage) | 210 | `nyc mocha build/test` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 206 | `mocha dist/test.js` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 205 | `cross-env NODE_ENV=test mocha --exit` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 203 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [Zarel/Pokemon-Showdown-Client](https://github.com/Zarel/Pokemon-Showdown-Client) | 201 | `eslint --config=.eslintrc.js --cache --cache-file=eslint-cache/base js/ data/ && eslint --config=build-tools/.eslintrc.js --cache --cache-file=eslint-cache/build build-tools/update build-tools/build-indexes && tslint --project . && tsc && node build && mocha` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 200 | `mocha -R spec test/integration` | 
| [R-js/blasjs](https://github.com/R-js/blasjs) | 199 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 197 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [bmewburn/intelephense](https://github.com/bmewburn/intelephense) | 197 | `mocha -r ts-node/register test/*.ts` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 196 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 195 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 188 | `mocha js` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 186 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 185 | `mocha lib/spec/core` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 185 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 184 | `nyc mocha --recursive test/**/*.ts` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 175 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 175 | `npm run build && npm run mocha` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 173 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 173 | `npm run lint && npm run mocha` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 172 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | 172 | `nyc mocha` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 168 | `tsc && cd dist && mocha` | 
| [emmanueltouzery/prelude-ts](https://github.com/emmanueltouzery/prelude-ts) | 168 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 166 | `npm run clean && npm run build && npm run lint && mocha` | 
| [Chinachu/Mirakurun](https://github.com/Chinachu/Mirakurun) | 164 | `mocha --exit test/*.spec.js` | 
| [nodejs/llhttp](https://github.com/nodejs/llhttp) | 162 | `npm run mocha && npm run lint` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 161 | `gulp compile && mocha --timeout 10000 -u tdd ./out/tests/` | 
| [googleapis/nodejs-translate](https://github.com/googleapis/nodejs-translate) | 156 | `nyc mocha build/test` | 
| [p-society/typeracer-cli](https://github.com/p-society/typeracer-cli) | 155 | `mocha --no-deprecation --timeout 10000 --require ts-node/register **/*.spec.ts` | 
| [PeterDing/chord](https://github.com/PeterDing/chord) | 154 | `./node_modules/mocha/bin/mocha --delay` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 154 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 153 | `mocha --require ts-node/register test/**/*.ts` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 152 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 147 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 146 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 145 | `gulp compile && mocha` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 145 | `mocha -r ts-node/register test/*.ts` | 
| [calidion/vig](https://github.com/calidion/vig) | 144 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 142 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 142 | `mocha lib/test` | 
| [cartant/rxjs-marbles](https://github.com/cartant/rxjs-marbles) | 136 | `yarn run lint && yarn run test:build && cross-env FAILING=0 yarn run test:ava && cross-env FAILING=0 yarn run test:jasmine && cross-env FAILING=0 yarn run test:jasmine-angular && cross-env FAILING=0 yarn run test:jest && cross-env FAILING=0 yarn run test:mocha && cross-env FAILING=0 yarn run test:tape` | 
| [Azure/azure-functions-pack](https://github.com/Azure/azure-functions-pack) | 136 | `npm run build && mocha --compilers ts:ts-node/register --recursive test/**/*-spec.ts` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 136 | `mocha` | 
| [nspragg/filehound](https://github.com/nspragg/filehound) | 135 | `mocha -r ts-node/register test/*.ts` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 134 | `npm run-script build && mocha --opts test/mocha.opts build/test/config.js build/test` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 133 | `mocha test/unit/ --exit` | 
| [TrustWallet/trust-ray](https://github.com/TrustWallet/trust-ray) | 133 | `cross-env NODE_ENV=test mocha --recursive --require ts-node/register 'test/**/*.test.ts' --exit` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 133 | `nyc --reporter=html --reporter=text mocha` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 132 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [DotJoshJohnson/vscode-xml](https://github.com/DotJoshJohnson/vscode-xml) | 132 | `npm run compile && mocha ./out/test/**/*.js` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 132 | `mocha --require espower-typescript/guess "test/**/*.test.ts"` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 130 | `TEST_BROWSER_DRIVER=puppeteer meteor test --driver-package=ardatan:mocha --raw-logs` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 129 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 129 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 129 | `mocha` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 128 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 128 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [rtfeldman/node-elm-compiler](https://github.com/rtfeldman/node-elm-compiler) | 128 | `rm -rf test/fixtures/elm-stuff && mocha test/**/*.ts --require ts-node/register --watch-extensions ts` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 127 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [vrimar/construct-ui](https://github.com/vrimar/construct-ui) | 127 | `cross-env TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [Microsoft/typescript-tslint-plugin](https://github.com/Microsoft/typescript-tslint-plugin) | 126 | `mocha ./out/**/*.test.js --slow 2000 --timeout 10000` | 
| [Soluto/graphql-to-mongodb](https://github.com/Soluto/graphql-to-mongodb) | 126 | `ts-mocha tests/**/*.spec.ts` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 126 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 126 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 124 | `istanbul test -- _mocha` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 124 | `mocha --require source-map-support/register dist/test` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 123 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [prh/prh](https://github.com/prh/prh) | 123 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 123 | `mocha test` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 122 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 121 | `mocha --timeout 10000` | 
| [colyseus/colyseus.js](https://github.com/colyseus/colyseus.js) | 120 | `mocha test/*.ts --require ts-node/register` | 
| [arfedulov/semantic-ui-calendar-react](https://github.com/arfedulov/semantic-ui-calendar-react) | 119 | `npx cross-env TS_NODE_COMPILER_OPTIONS="{""allowJs"":true}" npx mocha -r ts-node/register ./test/setup.js ./test/**/*.{js,jsx,ts,tsx}` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 119 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 119 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [dsherret/ts-nameof](https://github.com/dsherret/ts-nameof) | 119 | `yarn run --silent copy-test-files && nyc --reporter=lcov mocha --opts mocha.opts` | 
| [nomiclabs/buidler](https://github.com/nomiclabs/buidler) | 118 | `nyc mocha` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 118 | `mocha` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 117 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 115 | `cross-env NODE_ENV=test mocha --exit` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 114 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 113 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 113 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 112 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 111 | `mocha --full-trace tests/test.js  --reporter mocha-multi-reporters` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 109 | `npm run lint && node_modules/.bin/nyc npm run mocha` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 109 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 109 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 108 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 107 | `mocha --recursive -t 4000` | 
| [Esri/react-arcgis](https://github.com/Esri/react-arcgis) | 107 | `nyc mocha` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 107 | `mocha -R spec dist/test/**/*.js` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 107 | `webpack && mocha-phantomjs test/index.html` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 107 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 106 | `mocha --require ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 106 | `npm-run-all build test:mocha test:coverage lint` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 105 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 104 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 104 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 102 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 102 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 102 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 101 | `nyc npm run _mocha` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 101 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 100 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 100 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 99 | `mocha` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 99 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [nodejs/llparse](https://github.com/nodejs/llparse) | 99 | `npm run mocha && npm run lint` | 
| [wildbit/postmark.js](https://github.com/wildbit/postmark.js) | 99 | `node_modules/mocha/bin/mocha --timeout 10000 --retries 1 -r ts-node/register test/**/*test.ts` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 98 | `tsc; mocha --recursive lib/ test/runner` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 98 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 97 | `mocha ./spec/*.js` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 97 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 96 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [nucleojs/nucleo](https://github.com/nucleojs/nucleo) | 95 | `mocha -r ts-node/register` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 94 | `npm run lint && npm run prettier && npm run mocha` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 94 | `mocha test/* --timeout 500000` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 93 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 93 | `node node_modules/mocha/bin/mocha` | 
| [googleapis/nodejs-pubsub](https://github.com/googleapis/nodejs-pubsub) | 93 | `nyc mocha build/test` | 
| [Odi-ts/odi](https://github.com/Odi-ts/odi) | 93 | `nyc mocha test/**/*.test.ts` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 92 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 92 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 92 | `TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 91 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register 'test/**/*.ts'` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 91 | `mocha test/ --recursive` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 91 | `mocha` | 
| [levjj/esverify](https://github.com/levjj/esverify) | 91 | `TS_NODE_TRANSPILE_ONLY=true mocha -r ts-node/register tests/*.ts` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 90 | `mocha ./dist/test --recursive` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 88 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 87 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 86 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [bpatrik/pigallery2](https://github.com/bpatrik/pigallery2) | 84 | `ng test && mocha --recursive test/backend/unit && mocha --recursive test/backend/integration  && mocha --recursive test/common/unit ` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 83 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 83 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 82 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 81 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 81 | `mocha --require ts-node/register test/**/*.ts` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 81 | `mocha --ui tdd out/test/extension.test.js` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 81 | `mocha` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 80 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 79 | `mocha -r ./src/test/common/setup.ts ./lib/src/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 78 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 78 | `nyc mocha` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 78 | `mocha --compilers js:babel-core/register --recursive` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 78 | `npm run lint && npm run mocha` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 74 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 74 | `mocha -r ts-node/register 'test/main.js'` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 74 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 74 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 73 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 72 | `mocha -u tdd ./out/tests/` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 72 | `nyc mocha lib/**/*Test.js` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 71 | `mocha out/**/*.spec.js` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 71 | `mocha --timeout 10000 --slow 2500 tests/unittests/**/*.spec.js tests/functional-test-cases.js` | 
| [googleapis/nodejs-datastore](https://github.com/googleapis/nodejs-datastore) | 71 | `nyc mocha build/test` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 74 | `mocha -r ts-node/register 'test/main.js'` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 74 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 74 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 73 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 72 | `mocha -u tdd ./out/tests/` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 72 | `nyc mocha lib/**/*Test.js` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 72 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 72 | `TS_NODE_FILES=true mocha --opts src/test/mocha.opts "src/test/test*.ts"` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 71 | `mocha out/**/*.spec.js` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 71 | `mocha --timeout 10000 --slow 2500 tests/unittests/**/*.spec.js tests/functional-test-cases.js` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [googleapis/nodejs-datastore](https://github.com/googleapis/nodejs-datastore) | 71 | `nyc mocha build/test` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 70 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 69 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [rpgeeganage/async-ray](https://github.com/rpgeeganage/async-ray) | 69 | `nyc mocha` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 69 | `npm run compile && mocha && npm run lint` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 69 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 69 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 68 | `mocha .tmp/spec/index.spec.js` | 
| [roblox-ts/roblox-ts](https://github.com/roblox-ts/roblox-ts) | 68 | `nyc --reporter=html mocha --timeout 0 --require ts-node/register --require source-map-support/register --recursive src/test.ts && lua tests/spec.lua` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 67 | `mocha -r ts-node/register test/*.ts` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [puzzle-js/PuzzleJs](https://github.com/puzzle-js/PuzzleJs) | 66 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 66 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 66 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 65 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 64 | `mocha --opts spec/mocha.opts spec/**/*-spec.ts` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 64 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 64 | `nyc mocha` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 63 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 63 | `nyc mocha build/test` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 63 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd ./out/test/extension.test.js` | 
| [JustClear/colority](https://github.com/JustClear/colority) | 62 | `mocha test/index.js` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 62 | `mocha 'lib/**/__tests__/*.js'` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 62 | `mocha dist/test/*.js` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 61 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 61 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 61 | `nyc mocha --opts .mocha.opts` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 60 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 60 | `mocha build/tests/index.js` | 
| [wix/rawss](https://github.com/wix/rawss) | 60 | `mocha` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 60 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 60 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 60 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [DhyanaChina/koa2-typescript-guide](https://github.com/DhyanaChina/koa2-typescript-guide) | 59 | `mocha` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 59 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 58 | `mocha --timeout 30000 test/**/*.js` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 57 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 57 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 57 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 57 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 56 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 56 | `node_modules/.bin/mocha --watch` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 56 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [mono/TsToCSharp](https://github.com/mono/TsToCSharp) | 56 | `npm run lint && mocha  ./dist/TsToCSharpTests.js` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 55 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [lukeautry/ts-app](https://github.com/lukeautry/ts-app) | 55 | `cross-env TS_NODE_PROJECT=./api/tsconfig.json mocha -t 15000 -r ts-node/register "./api/**/*.spec.ts"` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 55 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 54 | `npm run compile && mocha` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 54 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 54 | `npm run build && npm run mocha` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 54 | `mocha` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 54 | `mocha --recursive --reporter-options mochaFile=report.xml --reporter mocha-junit-reporter` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 54 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 53 | `mocha --ui qunit` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 53 | `mocha` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 53 | `mocha --opts test/mocha.opts` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 53 | `mocha` | 
| [hg-pyun/iterize](https://github.com/hg-pyun/iterize) | 53 | `mocha --recursive ./test/*.ts --require ts-node/register` | 
| [nhabuiduc/react-filter-box](https://github.com/nhabuiduc/react-filter-box) | 53 | `node --max-old-space-size=16000 ./node_modules/.bin/mocha-webpack --require ignore-styles -r jsdom-global/register --webpack-config webpack.test.config.js --watch "./test/**/*.ts"` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 53 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 53 | `nyc mocha` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 52 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 52 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 51 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 51 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [woutervh-/typescript-is](https://github.com/woutervh-/typescript-is) | 50 | `ttsc --project tsconfig-test.json && mocha` | 
| [voodooattack/serialism](https://github.com/voodooattack/serialism) | 50 | `nyc mocha --expose-gc --ui mocha-typescript test/test_**.ts` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [VoxaAI/voxa](https://github.com/VoxaAI/voxa) | 50 | `mocha test/*.spec.* test/**/*.spec.*` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 50 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 50 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 49 | `mocha --opts config/mocha.opts` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 49 | `cross-env NODE_ENV=test mocha` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 49 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 49 | `npm run compile && mocha && npm run lint` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 49 | `mocha --compilers ts:ts-node/register --recursive` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 51 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [woutervh-/typescript-is](https://github.com/woutervh-/typescript-is) | 50 | `ttsc --project tsconfig-test.json && mocha` | 
| [voodooattack/serialism](https://github.com/voodooattack/serialism) | 50 | `nyc mocha --expose-gc --ui mocha-typescript test/test_**.ts` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [VoxaAI/voxa](https://github.com/VoxaAI/voxa) | 50 | `mocha test/*.spec.* test/**/*.spec.*` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 50 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 50 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 49 | `mocha --opts config/mocha.opts` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 49 | `cross-env NODE_ENV=test mocha` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 49 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 49 | `npm run compile && mocha && npm run lint` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 49 | `mocha --compilers ts:ts-node/register --recursive` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 49 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [teppeis/closure-ts](https://github.com/teppeis/closure-ts) | 49 | `npm-run-all --aggregate-output -p lint:ts build -p lint:js mocha` | 
| [balmbees/dynamo-types](https://github.com/balmbees/dynamo-types) | 49 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 48 | `mocha --opts mocha.opts --watch` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 48 | `mocha --require ts-node/register tests/**/*.ts` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 48 | `cross-env NODE_ENV=test mocha test/**/*.ts` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 48 | `mocha out/test` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 48 | `nyc mocha --opts test/mocha.opts` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 47 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 47 | `npm run prettier && npm run lint && npm run mocha` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 47 | `mocha` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 47 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 47 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 47 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [SPGoding/spu](https://github.com/SPGoding/spu) | 47 | `mocha --require espower-typescript/guess "./src/test/**/*.ts"` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 46 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [sourcegraph/browser-extensions](https://github.com/sourcegraph/browser-extensions) | 46 | `mocha --require ts-node/register --watch --watch-extensions ts './src/**/*.test.ts?(x)'` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 46 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 46 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [NativeScript/nativescript-dev-appium](https://github.com/NativeScript/nativescript-dev-appium) | 45 | `mocha --timeout 999999` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 45 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 45 | `mocha -R spec ./test` | 
| [aykutkardas/Json-Function](https://github.com/aykutkardas/Json-Function) | 45 | `cross-env TS_NODE_COMPILER_OPTIONS='{ "module": "commonjs" }' mocha -r ts-node/register -r ignore-styles -r jsdom-global/register test/**/*.spec.ts` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 45 | `mocha --reporter spec` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 44 | `nyc mocha build/test` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 44 | `mocha` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 44 | `mocha test` | 
| [ashleydavis/grademark](https://github.com/ashleydavis/grademark) | 44 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 44 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 44 | `nyc mocha build/test` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 44 | `mocha` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 44 | `mocha test` | 
| [ashleydavis/grademark](https://github.com/ashleydavis/grademark) | 44 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 44 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 43 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 43 | `npm run lint && mocha dist/spec` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 43 | `node_modules/.bin/mocha` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 43 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 43 | `mocha --recursive` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 43 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 43 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 43 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 43 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 43 | `nyc mocha --require source-map-support/register --require ts-node/register test/**/*.ts` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 42 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 42 | `mocha --opts cli-test-mocha.opts` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 42 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 42 | `mocha out/{,**/}*.spec.js -s 0` | 
| [ethereum-ts/evm-ts](https://github.com/ethereum-ts/evm-ts) | 42 | `yarn lint && yarn test:mocha` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 42 | `mocha && npm run aplus` | 
| [Pushwoosh/web-push-notifications](https://github.com/Pushwoosh/web-push-notifications) | 42 | `mocha` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 42 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 41 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 41 | `tsc && mocha build/test` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 41 | `mocha index.test.js` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 41 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 41 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 40 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [Jiasm/typescript-example](https://github.com/Jiasm/typescript-example) | 40 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 40 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 40 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 40 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [webix-hub/webix-jet](https://github.com/webix-hub/webix-jet) | 40 | `webpack && phantomjs node_modules/mocha-phantomjs-core/mocha-phantomjs-core.js tests/index.html spec` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 39 | `tsc && npm run lint && mocha` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 39 | `mocha --opts ./mocha.opts` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 39 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 39 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [azu/localstorage-ponyfill](https://github.com/azu/localstorage-ponyfill) | 39 | `mocha "test/**/*.ts"` | 
| [gcanti/hyper-ts](https://github.com/gcanti/hyper-ts) | 39 | `npm run prettier && npm run lint && npm run typings-checker && npm run mocha` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 39 | `npm run mocha && npm run lint` | 
| [aurelia/bundler](https://github.com/aurelia/bundler) | 39 | `mocha --reporter spec --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 39 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 38 | `tsc && mocha dist/**/*.spec.js` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 38 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 38 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 37 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 37 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 37 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [pokemongo-dev-contrib/pokemongo-json-pokedex](https://github.com/pokemongo-dev-contrib/pokemongo-json-pokedex) | 37 | `mocha --recursive --compilers ts:ts-node/register,ts:tsconfig-paths/register test/*.ts test/**/*.ts` | 
| [BeTomorrow/ReImproveJS](https://github.com/BeTomorrow/ReImproveJS) | 37 | `mocha --reporter spec --compilers ts:ts-node/register 'test/*.spec.ts' --timeout 120000` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 37 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 37 | `atool-test-mocha ./src/**/*-test.js` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 37 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 37 | `tsc && mocha spec/` | 
| [ProjectOpenSea/opensea-js](https://github.com/ProjectOpenSea/opensea-js) | 36 | `./node_modules/.bin/mocha test/*.ts --require ts-node/register --timeout 10000` | 
| [Polymer/polymer-linter](https://github.com/Polymer/polymer-linter) | 36 | `npm run build && mocha && npm run lint` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 36 | `mocha test/*.spec.ts` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 36 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 36 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [paralin/grpc-bus](https://github.com/paralin/grpc-bus) | 36 | `npm run lint && npm run mocha` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 36 | `mocha --recursive "dist/**/*.test.js"` | 
| [infinum/mobx-collection-store](https://github.com/infinum/mobx-collection-store) | 36 | `NODE_ENV=test nyc mocha` | 
| [fyndme/messenger-bot-tester](https://github.com/fyndme/messenger-bot-tester) | 35 | `mocha ./test-build` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 35 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 35 | `mocha` | 
| [tsframework/ts-framework](https://github.com/tsframework/ts-framework) | 35 | `mocha build-test --recursive` | 
| [agea/CmisJS](https://github.com/agea/CmisJS) | 35 | `tsc && mocha dist/**/*.spec.js` | 
| [shogogg/ts-option](https://github.com/shogogg/ts-option) | 35 | `mocha --reporter spec --compilers ts:espower-typescript/guess` | 
| [utopian-io/api.utopian.io](https://github.com/utopian-io/api.utopian.io) | 35 | `cross-env NODE_ENV=test npx mocha --ui bdd --reporter spec --colors --recursive -r ts-node/register tests/index.ts` | 
| [tuzhanai/captcha](https://github.com/tuzhanai/captcha) | 35 | `mocha -b --require ts-node/register --require source-map-support/register --recursive --exit src/test.ts` | 
| [ste-vg/pop.svg](https://github.com/ste-vg/pop.svg) | 35 | `nyc mocha --require ./mocha.config.js -r ts-node/register 'src/**/*.spec.ts'  --exit --recursive --timeout 10000` | 
| [aleixmorgadas/nem-library-ts](https://github.com/aleixmorgadas/nem-library-ts) | 35 | `mocha --ui bdd --recursive ./dist/test ./dist/integration_test --timeout 60000` | 
| [secret-tech/backend-token-wallets](https://github.com/secret-tech/backend-token-wallets) | 35 | `mocha -r ts-node/register -r test/prepare.ts src/**/*.spec.ts` | 
| [mrmlnc/vscode-stylefmt](https://github.com/mrmlnc/vscode-stylefmt) | 34 | `mocha out/**/*.spec.js -s 0` | 
| [mixi-inc/css-semdiff](https://github.com/mixi-inc/css-semdiff) | 34 | `mocha --opts mocha.opts './dist/**/*.test.js'` | 
| [leizongmin/leizm-web](https://github.com/leizongmin/leizm-web) | 34 | `npm run format && mocha --require ts-node/register --exit "src/test/**/*.ts"` | 
| [josephg/statecraft](https://github.com/josephg/statecraft) | 34 | `mocha -r ts-node/register test/*.ts` | 
| [Draccoz/twc](https://github.com/Draccoz/twc) | 34 | `npm run lint && mocha --require ts-node/register --ui bdd tests/tests.spec.ts` | 
| [davetemplin/web-request](https://github.com/davetemplin/web-request) | 34 | `mocha` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 34 | `tsc -p .tsconfig.test.json && mocha` | 
| [forthright/vile](https://github.com/forthright/vile) | 34 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [supergraphql/supergraph](https://github.com/supergraphql/supergraph) | 34 | `nyc mocha ./dist/**/*.spec.js` | 
| [Azure/oav](https://github.com/Azure/oav) | 33 | `npm run tsc && npm run tslint && nyc mocha ./dist/test/**/*.js -t 10000 --reporter mocha-junit-reporter --reporter spec` | 
| [acrazing/mobx-sync](https://github.com/acrazing/mobx-sync) | 33 | `mocha --require ts-node/register --slow 1000 ./src/**/*.spec.ts` | 
| [laurence-myers/tsdv-joi](https://github.com/laurence-myers/tsdv-joi) | 33 | `mocha --require source-map-support/register "dist/test/**/*.js"` | 
| [davetemplin/async-parallel](https://github.com/davetemplin/async-parallel) | 33 | `mocha` | 
| [nemtech/nem2-sdk-typescript-javascript](https://github.com/nemtech/nem2-sdk-typescript-javascript) | 33 | `mocha --ui bdd --recursive ./dist/test --timeout 90000` | 
| [userpixel/typescript](https://github.com/userpixel/typescript) | 33 | `mocha test` | 
| [mulesoft-labs/yaml-ast-parser](https://github.com/mulesoft-labs/yaml-ast-parser) | 33 | `npm run build && mocha --ui tdd dist/test` | 
| [olivierlsc/swagger-express-ts](https://github.com/olivierlsc/swagger-express-ts) | 33 | `echo "Testing..." && npm run build && nyc mocha` | 
| [tbluemel/rtf.js](https://github.com/tbluemel/rtf.js) | 33 | `mocha test/test.js` | 
| [qtumproject/qtumjs](https://github.com/qtumproject/qtumjs) | 33 | `mocha  lib/*_test.js` | 