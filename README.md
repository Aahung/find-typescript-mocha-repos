# Find Repos in TypeScript Tested using Mocha

The list was updated at 01:55:50 01/02/19 PST

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 66574 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 16474 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 11367 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 10019 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 7010 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 6247 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 5392 | `npm run mocha` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4623 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4473 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 3988 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3394 | `mocha --opts mocha.opts` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2850 | `mocha` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 2831 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2807 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [electron-userland/electron-forge](https://github.com/electron-userland/electron-forge) | 2441 | `cross-env TS_NODE_FILES=true yarn run mocha './tools/test-globber.ts' --opts mocha.opts` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2432 | `mocha 'test/**/*.ts'` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2223 | `mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [rrweb-io/rrweb](https://github.com/rrweb-io/rrweb) | 2025 | `npm run bundle:browser && cross-env TS_NODE_CACHE=false TS_NODE_FILES=true mocha -r ts-node/register test/**/*.test.ts` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1881 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1873 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1800 | `mocha` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1755 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1430 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1407 | `nyc -x '' mocha` | 
| [colyseus/colyseus](https://github.com/colyseus/colyseus) | 1390 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 1297 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1262 | `mocha --opts mocha.opts` | 
| [shanalikhan/code-settings-sync](https://github.com/shanalikhan/code-settings-sync) | 1259 | `npm run tslint-check && tsc -p ./ && mocha --recursive "./out/test/**/*.js"` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1232 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [funkia/list](https://github.com/funkia/list) | 1224 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [cherow/cherow](https://github.com/cherow/cherow) | 1209 | `cross-env TS_NODE_PROJECT="test/tsconfig.json" mocha test/**/*.ts -c -R progress -r ts-node/register -r source-map-support/register --recursive --globals expect` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1199 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [google/clasp](https://github.com/google/clasp) | 1125 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1122 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1096 | `nyc --reporter=html --reporter=text mocha` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 1048 | `tsc -p ./ && mocha` | 
| [itchio/itch](https://github.com/itchio/itch) | 976 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 934 | `mocha --opts test/mocha.opts` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 920 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 871 | `mocha bin/tests/test.js` | 
| [netgusto/nodebook](https://github.com/netgusto/nodebook) | 769 | `mocha test/backend` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 744 | `mocha --compilers ts:ts-node/register test/*.js || true` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 735 | `yarn run lint && yarn run test:mocha` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 711 | `mocha` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 710 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 706 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 679 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 673 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 665 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 648 | `mocha --recursive` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 611 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 608 | `mocha "out/**/*.spec.js" -s 0` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 601 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 591 | `npm run lint && npm run mocha` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 568 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [googleapis/google-auth-library-nodejs](https://github.com/googleapis/google-auth-library-nodejs) | 563 | `nyc mocha build/test` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 561 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 554 | `mocha test` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 552 | `mocha` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 551 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 547 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 536 | `mocha --opts test/mocha.opts dist/test` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 529 | `mocha test/unit` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 527 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 526 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [dsherret/ts-simple-ast](https://github.com/dsherret/ts-simple-ast) | 498 | `cross-env TS_NODE_COMPILER="ttypescript" TS_NODE_TRANSPILE_ONLY="true" mocha --opts mocha.opts --grep @performance --invert` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 486 | `mocha --opts mocha.opts` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 475 | `mocha --opts mocha.opts` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 474 | `cross-env NODE_ENV=tsoa_test mocha **/*.spec.ts --exit --compilers ts:ts-node/register` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 469 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 462 | `npm run build && mocha` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 458 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 453 | `npm run mocha` | 
| [Cookie-AutoDelete/Cookie-AutoDelete](https://github.com/Cookie-AutoDelete/Cookie-AutoDelete) | 446 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec ./test/*` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 444 | `_mocha --` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 444 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 442 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 442 | `cd test && mocha -r ts-node/register *.ts` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 436 | `tsc && mocha test && yarn lint` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 420 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 399 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 396 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 392 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 384 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [R-js/libRmath.js](https://github.com/R-js/libRmath.js) | 378 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 361 | `mocha` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 353 | `npm run build && mocha` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 347 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 336 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 334 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 327 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 310 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 307 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 306 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 294 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 294 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 292 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts view/test/test-heightmap.ts` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 291 | `mocha` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 291 | `mocha` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 289 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 286 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 283 | `mocha lib/test` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 275 | `mocha` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 274 | `mocha --compilers js:babel-register test/**/*.js` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 271 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 262 | `mocha src/**/*.spec.ts` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 251 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 249 | `mocha "test/**/*.spec.ts"` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 245 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 244 | `tsc && mocha dist/**/*.spec.js` | 
| [AmirTugi/tea-school](https://github.com/AmirTugi/tea-school) | 241 | `npx ts-mocha ./src/tests/**.ts` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 241 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 237 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 235 | `tsc && mocha` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 235 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 231 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 229 | `mocha-webpack "src/**/*.ts"` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 226 | `nyc --reporter html mocha` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 223 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 218 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 214 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 209 | `mocha test` | 
| [googleapis/nodejs-storage](https://github.com/googleapis/nodejs-storage) | 207 | `nyc mocha build/test` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 205 | `mocha dist/test.js` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 202 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 201 | `cross-env NODE_ENV=test mocha --exit` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 200 | `mocha -R spec test/integration` | 
| [Zarel/Pokemon-Showdown-Client](https://github.com/Zarel/Pokemon-Showdown-Client) | 199 | `eslint --config=.eslintrc.js --cache --cache-file=eslint-cache/base js/ data/ && eslint --config=build-tools/.eslintrc.js --cache --cache-file=eslint-cache/build build-tools/update build-tools/build-indexes && tslint --project . && tsc && node build && mocha` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 197 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [R-js/blasjs](https://github.com/R-js/blasjs) | 197 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [bmewburn/intelephense](https://github.com/bmewburn/intelephense) | 195 | `mocha -r ts-node/register test/*.ts` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 194 | `cd test && mocha -r ts-node/register *.ts` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 193 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 190 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 187 | `mocha js` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 184 | `nyc mocha --recursive test/**/*.ts` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 184 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 184 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 182 | `mocha lib/spec/core` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 175 | `npm run build && npm run mocha` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 174 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 173 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 173 | `npm run lint && npm run mocha` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 172 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | 170 | `nyc mocha` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 168 | `tsc && cd dist && mocha` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 166 | `npm run clean && npm run build && npm run lint && mocha` | 
| [emmanueltouzery/prelude-ts](https://github.com/emmanueltouzery/prelude-ts) | 164 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [nodejs/llhttp](https://github.com/nodejs/llhttp) | 162 | `npm run mocha && npm run lint` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 160 | `gulp compile && mocha --timeout 10000 -u tdd ./out/tests/` | 
| [Chinachu/Mirakurun](https://github.com/Chinachu/Mirakurun) | 159 | `mocha --exit test/*.spec.js` | 
| [googleapis/nodejs-translate](https://github.com/googleapis/nodejs-translate) | 156 | `nyc mocha build/test` | 
| [p-society/typeracer-cli](https://github.com/p-society/typeracer-cli) | 155 | `mocha --no-deprecation --timeout 10000 --require ts-node/register **/*.spec.ts` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 153 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 152 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [PeterDing/chord](https://github.com/PeterDing/chord) | 151 | `./node_modules/mocha/bin/mocha --delay` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 149 | `mocha --require ts-node/register test/**/*.ts` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 147 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 146 | `mocha -r ts-node/register test/*.ts` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 145 | `tsc && mocha` | 
| [calidion/vig](https://github.com/calidion/vig) | 144 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 144 | `gulp compile && mocha` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 142 | `mocha lib/test` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 139 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 138 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [Azure/azure-functions-pack](https://github.com/Azure/azure-functions-pack) | 137 | `npm run build && mocha --compilers ts:ts-node/register --recursive test/**/*-spec.ts` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 136 | `mocha` | 
| [nspragg/filehound](https://github.com/nspragg/filehound) | 134 | `mocha -r ts-node/register test/*.ts` | 
| [DotJoshJohnson/vscode-xml](https://github.com/DotJoshJohnson/vscode-xml) | 133 | `npm run compile && mocha ./out/test/**/*.js` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 132 | `mocha test/unit/ --exit` | 
| [TrustWallet/trust-ray](https://github.com/TrustWallet/trust-ray) | 132 | `cross-env NODE_ENV=test mocha --recursive --require ts-node/register 'test/**/*.test.ts' --exit` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 132 | `nyc --reporter=html --reporter=text mocha` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 131 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 130 | `npm run-script build && mocha --opts test/mocha.opts build/test/config.js build/test` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 130 | `TEST_BROWSER_DRIVER=puppeteer meteor test --driver-package=ardatan:mocha --raw-logs` | 
| [cartant/rxjs-marbles](https://github.com/cartant/rxjs-marbles) | 129 | `yarn run lint && yarn run test:build && cross-env FAILING=0 yarn run test:ava && cross-env FAILING=0 yarn run test:jasmine && cross-env FAILING=0 yarn run test:jasmine-angular && cross-env FAILING=0 yarn run test:jest && cross-env FAILING=0 yarn run test:mocha && cross-env FAILING=0 yarn run test:tape` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 129 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 129 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 128 | `mocha --require espower-typescript/guess "test/**/*.test.ts"` | 
| [rtfeldman/node-elm-compiler](https://github.com/rtfeldman/node-elm-compiler) | 127 | `rm -rf test/fixtures/elm-stuff & mocha test/**/*.ts --require ts-node/register --watch-extensions ts` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 126 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 126 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 126 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [Soluto/graphql-to-mongodb](https://github.com/Soluto/graphql-to-mongodb) | 125 | `ts-mocha tests/**/*.spec.ts` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 125 | `mocha` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 125 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 124 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 124 | `istanbul test -- _mocha` | 
| [prh/prh](https://github.com/prh/prh) | 124 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 124 | `mocha --require source-map-support/register dist/test` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 123 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 123 | `mocha test` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 121 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 121 | `mocha --timeout 10000` | 
| [colyseus/colyseus.js](https://github.com/colyseus/colyseus.js) | 120 | `mocha test/*.ts --require ts-node/register` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 119 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [vrimar/construct-ui](https://github.com/vrimar/construct-ui) | 117 | `cross-env TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [Microsoft/typescript-tslint-plugin](https://github.com/Microsoft/typescript-tslint-plugin) | 117 | `mocha ./out/**/*.test.js --slow 2000 --timeout 10000` | 
| [dsherret/ts-nameof](https://github.com/dsherret/ts-nameof) | 117 | `yarn run --silent copy-test-files && nyc --reporter=lcov mocha --opts mocha.opts` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 116 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 116 | `cross-env NODE_ENV=test mocha --exit` | 
| [nomiclabs/buidler](https://github.com/nomiclabs/buidler) | 116 | `nyc mocha` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 116 | `mocha` | 
| [arfedulov/semantic-ui-calendar-react](https://github.com/arfedulov/semantic-ui-calendar-react) | 114 | `npx cross-env TS_NODE_COMPILER_OPTIONS="{""allowJs"":true}" npx mocha -r ts-node/register ./test/setup.js ./test/**/*.{js,jsx,ts,tsx}` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 114 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 112 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 110 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 110 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 110 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 109 | `npm run lint && node_modules/.bin/nyc npm run mocha` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 109 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 108 | `mocha --full-trace tests/test.js  --reporter mocha-multi-reporters` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 107 | `mocha --recursive -t 4000` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 107 | `mocha -R spec dist/test/**/*.js` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 107 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 107 | `webpack && mocha-phantomjs test/index.html` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 107 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 107 | `mocha --recursive -t 4000` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 107 | `mocha -R spec dist/test/**/*.js` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 107 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 107 | `webpack && mocha-phantomjs test/index.html` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 107 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 106 | `npm-run-all build test:mocha test:coverage lint` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 105 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 104 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 104 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [Esri/react-arcgis](https://github.com/Esri/react-arcgis) | 104 | `nyc mocha` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 103 | `mocha --require ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 102 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 102 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 102 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 101 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 100 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 100 | `mocha` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 100 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 100 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 99 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 98 | `tsc; mocha --recursive lib/ test/runner` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 98 | `nyc npm run _mocha` | 
| [nodejs/llparse](https://github.com/nodejs/llparse) | 98 | `npm run mocha && npm run lint` | 
| [wildbit/postmark.js](https://github.com/wildbit/postmark.js) | 98 | `node_modules/mocha/bin/mocha --timeout 10000 --retries 1 -r ts-node/register test/**/*test.ts` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 97 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 97 | `mocha ./spec/*.js` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 96 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [nucleojs/nucleo](https://github.com/nucleojs/nucleo) | 95 | `mocha -r ts-node/register` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 94 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 93 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 93 | `node node_modules/mocha/bin/mocha` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 93 | `mocha test/* --timeout 500000` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 92 | `npm run lint && npm run prettier && npm run mocha` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 92 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [googleapis/nodejs-pubsub](https://github.com/googleapis/nodejs-pubsub) | 92 | `nyc mocha build/test` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 91 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register 'test/**/*.ts'` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 91 | `mocha test/ --recursive` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 91 | `mocha` | 
| [levjj/esverify](https://github.com/levjj/esverify) | 91 | `TS_NODE_TRANSPILE_ONLY=true mocha -r ts-node/register tests/*.ts` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 90 | `mocha ./dist/test --recursive` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 89 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 88 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 87 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 86 | `TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 83 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 83 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 83 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [bpatrik/pigallery2](https://github.com/bpatrik/pigallery2) | 82 | `ng test && mocha --recursive test/backend/unit && mocha --recursive test/backend/integration  && mocha --recursive test/common/unit ` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 81 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 81 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 81 | `mocha --require ts-node/register test/**/*.ts` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 81 | `mocha` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 78 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 78 | `mocha -r ./src/test/common/setup.ts ./lib/src/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [CityOfZion/neo-js](https://github.com/CityOfZion/neo-js) | 78 | `mocha --reporter spec` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 77 | `npm run lint && npm run mocha` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 77 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [teambition/ReactiveDB](https://github.com/teambition/ReactiveDB) | 76 | `npm run lint && NODE_ENV=test tman --mocha spec-js/test/run.js` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 76 | `tsc && mocha "dist/test/**/*.js" ` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 76 | `nyc mocha` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 76 | `mocha --compilers js:babel-core/register --recursive` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 75 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 75 | `nyc mocha --recursive test/**/*.ts` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 75 | `nyc mocha build/test` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 75 | `npm run lint && nyc mocha` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 75 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 75 | `nyc mocha --recursive test/**/*.ts` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 75 | `nyc mocha build/test` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 75 | `npm run lint && nyc mocha` | 
| [Odi-ts/odi](https://github.com/Odi-ts/odi) | 75 | `nyc mocha test/**/*.test.ts` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 74 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 74 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 73 | `mocha -r ts-node/register 'test/main.js'` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 73 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 72 | `TS_NODE_FILES=true mocha --opts src/test/mocha.opts "src/test/test*.ts"` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 72 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 72 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 71 | `mocha -u tdd ./out/tests/` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [googleapis/nodejs-datastore](https://github.com/googleapis/nodejs-datastore) | 71 | `nyc mocha build/test` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 70 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 70 | `mocha out/**/*.spec.js` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 70 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 69 | `nyc mocha lib/**/*Test.js` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 69 | `npm run compile && mocha && npm run lint` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 69 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 68 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 68 | `mocha --timeout 10000 --slow 2500 tests/unittests/**/*.spec.js tests/functional-test-cases.js` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 68 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 67 | `mocha -r ts-node/register test/*.ts` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [roblox-ts/roblox-ts](https://github.com/roblox-ts/roblox-ts) | 67 | `nyc --reporter=html mocha --timeout 0 --require ts-node/register --require source-map-support/register --recursive src/test.ts && lua tests/spec.lua` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [puzzle-js/PuzzleJs](https://github.com/puzzle-js/PuzzleJs) | 65 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 65 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 65 | `mocha .tmp/spec/index.spec.js` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 65 | `nyc mocha` | 
| [rpgeeganage/async-ray](https://github.com/rpgeeganage/async-ray) | 64 | `nyc mocha` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 64 | `mocha --opts spec/mocha.opts spec/**/*-spec.ts` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 64 | `nyc mocha build/test` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 64 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 64 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 63 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 63 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 62 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 62 | `mocha 'lib/**/__tests__/*.js'` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 62 | `mocha dist/test/*.js` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 60 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 60 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [wix/rawss](https://github.com/wix/rawss) | 60 | `mocha` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 60 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 60 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 60 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 60 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd ./out/test/extension.test.js` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 59 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 59 | `nyc mocha --opts .mocha.opts` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 59 | `mocha build/tests/index.js` | 
| [teamdomy/domy-cli](https://github.com/teamdomy/domy-cli) | 59 | `mocha --reporter spec --require ts-node/register 'tests/**/*.spec.ts'` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 59 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 57 | `mocha --timeout 30000 test/**/*.js` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 57 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 56 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 56 | `node_modules/.bin/mocha --watch` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 56 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [DhyanaChina/koa2-typescript-guide](https://github.com/DhyanaChina/koa2-typescript-guide) | 55 | `mocha` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 55 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 55 | `mocha --recursive` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 55 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 55 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 54 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 54 | `npm run build && npm run mocha` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 54 | `mocha` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 54 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 53 | `mocha` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 53 | `mocha` | 
| [nhabuiduc/react-filter-box](https://github.com/nhabuiduc/react-filter-box) | 53 | `node --max-old-space-size=16000 ./node_modules/.bin/mocha-webpack --require ignore-styles -r jsdom-global/register --webpack-config webpack.test.config.js --watch "./test/**/*.ts"` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 53 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 53 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [mono/TsToCSharp](https://github.com/mono/TsToCSharp) | 53 | `npm run lint && mocha  ./dist/TsToCSharpTests.js` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 52 | `NODE_ENV=test nyc mocha` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 52 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 52 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [lukeautry/ts-app](https://github.com/lukeautry/ts-app) | 52 | `cross-env TS_NODE_PROJECT=./api/tsconfig.json mocha -t 15000 -r ts-node/register "./api/**/*.spec.ts"` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 52 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 52 | `nyc mocha` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 52 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 51 | `mocha --ui qunit` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 51 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 51 | `npm run compile && mocha` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 51 | `NODE_ENV=test nyc mocha` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 51 | `mocha --opts test/mocha.opts` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 51 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [DhyanaChina/todo-live](https://github.com/DhyanaChina/todo-live) | 51 | `mocha` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 50 | `mocha test/*.js` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 50 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 50 | `tsc --version && tsc && mocha out/test` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 50 | `nyc mocha` | 
| [voodooattack/serialism](https://github.com/voodooattack/serialism) | 50 | `nyc mocha --expose-gc --ui mocha-typescript test/test_**.ts` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 50 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 50 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 49 | `mocha --opts config/mocha.opts` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 49 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [teppeis/closure-ts](https://github.com/teppeis/closure-ts) | 49 | `npm-run-all --aggregate-output -p lint:ts build -p lint:js mocha` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 48 | `cross-env NODE_ENV=test mocha` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 48 | `mocha --opts mocha.opts --watch` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 48 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 48 | `nyc mocha --opts test/mocha.opts` | 
| [balmbees/dynamo-types](https://github.com/balmbees/dynamo-types) | 48 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 47 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 47 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 47 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 47 | `npm run compile && mocha && npm run lint` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 47 | `mocha --require ts-node/register tests/**/*.ts` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 47 | `mocha --compilers ts:ts-node/register --recursive` | 
| [hg-pyun/iterize](https://github.com/hg-pyun/iterize) | 47 | `mocha --recursive ./test/*.ts --require ts-node/register` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [CommandBlockLogic/spu](https://github.com/CommandBlockLogic/spu) | 47 | `mocha --require espower-typescript/guess "./src/test/**/*.ts"` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 46 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 46 | `npm run prettier && npm run lint && npm run mocha` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [sourcegraph/browser-extensions](https://github.com/sourcegraph/browser-extensions) | 46 | `mocha --require ts-node/register --watch --watch-extensions ts './src/**/*.test.ts?(x)'` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 46 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 46 | `mocha out/test` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 46 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 46 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 46 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 45 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 45 | `mocha --reporter spec` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 44 | `mocha` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 44 | `nyc mocha build/test` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 44 | `mocha` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 44 | `cross-env NODE_ENV=test mocha test/**/*.ts` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 44 | `mocha -R spec ./test` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 44 | `mocha test` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 43 | `npm run lint && mocha dist/spec` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 43 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [woutervh-/typescript-is](https://github.com/woutervh-/typescript-is) | 43 | `ttsc --project tsconfig-test.json && mocha` | 
| [NativeScript/nativescript-dev-appium](https://github.com/NativeScript/nativescript-dev-appium) | 43 | `mocha --timeout 999999` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 43 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 43 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 43 | `npm run lint && mocha dist/spec` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 43 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [woutervh-/typescript-is](https://github.com/woutervh-/typescript-is) | 43 | `ttsc --project tsconfig-test.json && mocha` | 
| [NativeScript/nativescript-dev-appium](https://github.com/NativeScript/nativescript-dev-appium) | 43 | `mocha --timeout 999999` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 43 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 43 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 43 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [ashleydavis/grademark](https://github.com/ashleydavis/grademark) | 43 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 43 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 43 | `nyc mocha --require source-map-support/register --require ts-node/register test/**/*.ts` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 42 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 42 | `mocha --opts cli-test-mocha.opts` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 42 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 42 | `mocha out/{,**/}*.spec.js -s 0` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 42 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 42 | `mocha --recursive` | 
| [Pushwoosh/web-push-notifications](https://github.com/Pushwoosh/web-push-notifications) | 42 | `mocha` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 42 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 41 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [Jiasm/typescript-example](https://github.com/Jiasm/typescript-example) | 41 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [ethereum-ts/evm-ts](https://github.com/ethereum-ts/evm-ts) | 41 | `yarn lint && yarn test:mocha` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 41 | `mocha && npm run aplus` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 41 | `tsc && mocha build/test` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 41 | `mocha index.test.js` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 41 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 41 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 40 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 40 | `node_modules/.bin/mocha` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 40 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 40 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 40 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [webix-hub/webix-jet](https://github.com/webix-hub/webix-jet) | 40 | `webpack && phantomjs node_modules/mocha-phantomjs-core/mocha-phantomjs-core.js tests/index.html spec` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 40 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 39 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 39 | `tsc && npm run lint && mocha` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 39 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 39 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [aurelia/bundler](https://github.com/aurelia/bundler) | 39 | `mocha --reporter spec --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 38 | `mocha --opts ./mocha.opts` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 38 | `tsc && mocha dist/**/*.spec.js` | 
| [azu/localstorage-ponyfill](https://github.com/azu/localstorage-ponyfill) | 38 | `mocha "test/**/*.ts"` | 
| [gcanti/hyper-ts](https://github.com/gcanti/hyper-ts) | 38 | `npm run prettier && npm run lint && npm run typings-checker && npm run mocha` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 38 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 38 | `npm run mocha && npm run lint` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 38 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 37 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 37 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 37 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 37 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 37 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 37 | `tsc && mocha spec/` | 
| [Polymer/polymer-linter](https://github.com/Polymer/polymer-linter) | 36 | `npm run build && mocha && npm run lint` | 
| [Pravez/ReImproveJS](https://github.com/Pravez/ReImproveJS) | 36 | `mocha --reporter spec --compilers ts:ts-node/register 'test/*.spec.ts' --timeout 120000` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 36 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 36 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 36 | `atool-test-mocha ./src/**/*-test.js` | 
| [paralin/grpc-bus](https://github.com/paralin/grpc-bus) | 36 | `npm run lint && npm run mocha` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 36 | `mocha --recursive "dist/**/*.test.js"` | 
| [fyndme/messenger-bot-tester](https://github.com/fyndme/messenger-bot-tester) | 35 | `mocha ./test-build` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 35 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 35 | `mocha` | 
| [agea/CmisJS](https://github.com/agea/CmisJS) | 35 | `tsc && mocha dist/**/*.spec.js` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 35 | `mocha test/*.spec.ts` | 
| [utopian-io/api.utopian.io](https://github.com/utopian-io/api.utopian.io) | 35 | `cross-env NODE_ENV=test npx mocha --ui bdd --reporter spec --colors --recursive -r ts-node/register tests/index.ts` | 
| [ste-vg/pop.svg](https://github.com/ste-vg/pop.svg) | 35 | `nyc mocha --require ./mocha.config.js -r ts-node/register 'src/**/*.spec.ts'  --exit --recursive --timeout 10000` | 
| [infinum/mobx-collection-store](https://github.com/infinum/mobx-collection-store) | 35 | `NODE_ENV=test nyc mocha` | 
| [secret-tech/backend-token-wallets](https://github.com/secret-tech/backend-token-wallets) | 35 | `mocha -r ts-node/register -r test/prepare.ts src/**/*.spec.ts` | 
| [mixi-inc/css-semdiff](https://github.com/mixi-inc/css-semdiff) | 34 | `mocha --opts mocha.opts './dist/**/*.test.js'` | 
| [tsframework/ts-framework](https://github.com/tsframework/ts-framework) | 34 | `mocha build-test --recursive` | 
| [josephg/statecraft](https://github.com/josephg/statecraft) | 34 | `mocha -r ts-node/register test/*.ts` | 
| [leizongmin/leizm-web](https://github.com/leizongmin/leizm-web) | 34 | `npm run format && mocha --require ts-node/register --exit "src/test/**/*.ts"` | 
| [Draccoz/twc](https://github.com/Draccoz/twc) | 34 | `npm run lint && mocha --require ts-node/register --ui bdd tests/tests.spec.ts` | 
| [davetemplin/web-request](https://github.com/davetemplin/web-request) | 34 | `mocha` | 
| [tuzhanai/captcha](https://github.com/tuzhanai/captcha) | 34 | `mocha -b --require ts-node/register --require source-map-support/register --recursive --exit src/test.ts` | 
| [forthright/vile](https://github.com/forthright/vile) | 34 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [supergraphql/supergraph](https://github.com/supergraphql/supergraph) | 34 | `nyc mocha ./dist/**/*.spec.js` | 
| [ProjectOpenSea/opensea-js](https://github.com/ProjectOpenSea/opensea-js) | 33 | `./node_modules/.bin/mocha test/*.ts --require ts-node/register --timeout 10000` | 
| [mrmlnc/vscode-stylefmt](https://github.com/mrmlnc/vscode-stylefmt) | 33 | `mocha out/**/*.spec.js -s 0` | 
| [nemtech/nem2-sdk-typescript-javascript](https://github.com/nemtech/nem2-sdk-typescript-javascript) | 33 | `mocha --ui bdd --recursive ./dist/test --timeout 90000` | 
| [userpixel/typescript](https://github.com/userpixel/typescript) | 33 | `mocha test` | 
| [mulesoft-labs/yaml-ast-parser](https://github.com/mulesoft-labs/yaml-ast-parser) | 33 | `npm run build && mocha --ui tdd dist/test` | 
| [tbluemel/rtf.js](https://github.com/tbluemel/rtf.js) | 33 | `mocha test/test.js` | 
| [qtumproject/qtumjs](https://github.com/qtumproject/qtumjs) | 33 | `mocha  lib/*_test.js` | 
| [aleixmorgadas/nem-library-ts](https://github.com/aleixmorgadas/nem-library-ts) | 33 | `mocha --ui bdd --recursive ./dist/test ./dist/integration_test --timeout 60000` | 
| [Azure/oav](https://github.com/Azure/oav) | 32 | `npm run tsc && npm run tslint && nyc mocha ./test/**/*.ts -r ts-node/register -t 10000 --reporter mocha-junit-reporter --reporter spec` | 
| [lebinh/cloudflare-workers](https://github.com/lebinh/cloudflare-workers) | 32 | `mocha -r ts-node/register 'tests/**/*_test.ts'` | 
| [Webtomizer/typeorm-loader](https://github.com/Webtomizer/typeorm-loader) | 32 | `npm run build && [ -d tests ] && NODE_ENV=test mocha $NODE_DEBUG_OPTION -r ts-node/register -r tslib tests/test_**.ts` | 
| [NikitchenkoSergey/scheme-designer](https://github.com/NikitchenkoSergey/scheme-designer) | 32 | `mocha` | 
| [OpenFinanceIO/smart-securities-standard](https://github.com/OpenFinanceIO/smart-securities-standard) | 32 | `tsc -p tsconfig.test.json && mocha dist/test/*.spec.js src/` | 
| [acrazing/mobx-sync](https://github.com/acrazing/mobx-sync) | 32 | `mocha --require ts-node/register --slow 1000 ./src/**/*.spec.ts` | 
| [davetemplin/async-parallel](https://github.com/davetemplin/async-parallel) | 32 | `mocha` | 
| [fsahmad/typescript-uml](https://github.com/fsahmad/typescript-uml) | 32 | `npm run build && mocha --compilers ts:ts-node/register --recursive 'src/**/*-spec.ts'` | 
| [igorzg/typeix](https://github.com/igorzg/typeix) | 32 | `npm run compile && mocha build/tests/ --debug --full-trace` | 
| [exercism/typescript](https://github.com/exercism/typescript) | 32 | `mocha test` | 
| [pokemongo-dev-contrib/pokemongo-json-pokedex](https://github.com/pokemongo-dev-contrib/pokemongo-json-pokedex) | 32 | `mocha --recursive --compilers ts:ts-node/register,ts:tsconfig-paths/register test/*.ts test/**/*.ts` | 
| [GoodgameStudios/RobotlegsJS](https://github.com/GoodgameStudios/RobotlegsJS) | 32 | `nyc mocha` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 32 | `tsc -p .tsconfig.test.json && mocha` | 