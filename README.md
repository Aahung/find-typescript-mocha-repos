# Find Repos in TypeScript Tested using Mocha

The list was updated at 00:44:00 09/20/18 PDT

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 59644 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 14856 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 8779 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 8251 | `tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 6756 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 5578 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 4758 | `npm run mocha` | 
| [Microsoft/sqlopsstudio](https://github.com/Microsoft/sqlopsstudio) | 4335 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 3955 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3249 | `mocha --opts mocha.opts` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2732 | `mocha` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 2523 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2402 | `mocha 'test/**/*.ts'` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 2523 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2402 | `mocha 'test/**/*.ts'` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2361 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 2022 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 1985 | `./node_modules/.bin/mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1787 | `mocha` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1778 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1722 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1646 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1316 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1233 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [wilk/microjob](https://github.com/wilk/microjob) | 1233 | `node --experimental-worker node_modules/.bin/_mocha -r ts-node/register ./test/**/*.ts` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1227 | `nyc -x '' mocha` | 
| [gamestdio/colyseus](https://github.com/gamestdio/colyseus) | 1178 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [funkia/list](https://github.com/funkia/list) | 1172 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1117 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [watson-developer-cloud/node-sdk](https://github.com/watson-developer-cloud/node-sdk) | 1112 | `nyc mocha test/unit/ test/integration/ && nyc report --reporter=html` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1075 | `nyc --reporter=html --reporter=text mocha` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1058 | `mocha --opts mocha.opts` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1034 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 979 | `tsc -p ./ && mocha` | 
| [itchio/itch](https://github.com/itchio/itch) | 912 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 901 | `mocha --opts test/mocha.opts` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 828 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [google/clasp](https://github.com/google/clasp) | 787 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 766 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 757 | `mocha bin/tests/test.js` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 716 | `yarn run lint && yarn run test:mocha` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 701 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 672 | `mocha` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 644 | `mocha --compilers ts:ts-node/register test/*.js || true` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 642 | `mocha --recursive` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 640 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 626 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 614 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 607 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 594 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 585 | `npm run lint && npm run mocha` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 568 | `mocha "out/**/*.spec.js" -s 0` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 534 | `mocha` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 532 | `mocha --opts test/mocha.opts dist/test` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 526 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 523 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 515 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 478 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 476 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 458 | `npm run build && mocha` | 
| [burtonator/polar-bookshelf](https://github.com/burtonator/polar-bookshelf) | 442 | `mocha-parallel-tests --timeout 10000 --max-parallel=1 --exit --recursive web/js/**/*Test.js` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 441 | `_mocha --` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 436 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 432 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 426 | `mocha --opts mocha.opts` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 418 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 418 | `mocha --opts mocha.opts` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 410 | `npm run mocha` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 394 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 389 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 384 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 383 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 382 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [Romakita/ts-express-decorators](https://github.com/Romakita/ts-express-decorators) | 381 | `npm run clean && npm run tsc && npm run tslint && cross-env NODE_ENV=test nyc --reporter=html --reporter=text _mocha --recursive` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 380 | `cross-env NODE_ENV=test mocha **/*.spec.ts --compilers ts:ts-node/register` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 373 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [jacobbogers/libRmath.js](https://github.com/jacobbogers/libRmath.js) | 360 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 357 | `mocha` | 
| [dsherret/ts-simple-ast](https://github.com/dsherret/ts-simple-ast) | 353 | `cross-env TS_NODE_COMPILER="ttypescript" mocha --opts mocha.opts` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 348 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 345 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 337 | `npm run build && mocha` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 334 | `cd test && mocha -r ts-node/register *.ts` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 318 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 315 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 289 | `mocha` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 288 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 282 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 278 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [Microsoft/node-pty](https://github.com/Microsoft/node-pty) | 273 | `cross-env NODE_ENV=test mocha -R spec --exit lib/*.test.js` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 269 | `mocha --compilers js:babel-register test/**/*.js` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 264 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 261 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 260 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 260 | `mocha` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 257 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 256 | `mocha src/**/*.spec.ts` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 255 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 253 | `mocha lib/test` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 252 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 249 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 239 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 231 | `tsc && mocha` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 229 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 225 | `nyc --reporter html mocha` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 222 | `mocha` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 212 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 207 | `mocha test` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 204 | `mocha test` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 202 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 200 | `tsc && mocha dist/**/*.spec.js` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 199 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 199 | `mocha -R spec test/integration` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 197 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 194 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts view/test/test-heightmap.ts` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 193 | `mocha dist/test.js` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 191 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 185 | `mocha js` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 185 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [ClickSimply/Nano-SQL](https://github.com/ClickSimply/Nano-SQL) | 181 | `mocha -r ts-node/register tests/index.ts` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 177 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [dubzzz/fast-check](https://github.com/dubzzz/fast-check) | 176 | `npm run build && nyc mocha "test/unit/**/*.spec.ts"` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 175 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 175 | `cross-env NODE_ENV=test mocha` | 
| [jacobbogers/blasjs](https://github.com/jacobbogers/blasjs) | 174 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [bmewburn/intelephense](https://github.com/bmewburn/intelephense) | 172 | `mocha -r ts-node/register test/*.ts` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 171 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 169 | `npm run lint && npm run mocha` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 168 | `nyc mocha --recursive test/**/*.ts` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 168 | `npm run clean && npm run build && npm run lint && mocha` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 164 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 152 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 151 | `mocha-webpack "src/**/*.ts"` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 146 | `mocha lib/spec/core` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 145 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [calidion/vig](https://github.com/calidion/vig) | 135 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 146 | `mocha lib/spec/core` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 145 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [calidion/vig](https://github.com/calidion/vig) | 135 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [emmanueltouzery/prelude.ts](https://github.com/emmanueltouzery/prelude.ts) | 135 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 133 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [Azure/azure-functions-pack](https://github.com/Azure/azure-functions-pack) | 132 | `npm run build && mocha --compilers ts:ts-node/register --recursive test/**/*-spec.ts` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 132 | `TEST_BROWSER_DRIVER=phantomjs meteor test --driver-package=ardatan:mocha` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 131 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 130 | `tsc && mocha` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 128 | `mocha` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 127 | `mocha test/unit/ --exit` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 127 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 127 | `mocha -r ts-node/register test/*.ts` | 
| [hydux/hydux](https://github.com/hydux/hydux) | 126 | `npm run mocha -- "src/test/unit/*.test.ts"` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 126 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 125 | `mocha --require ts-node/register test/**/*.ts` | 
| [nspragg/filehound](https://github.com/nspragg/filehound) | 125 | `mocha -r ts-node/register test/*.ts` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 124 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 124 | `npm run clean && tslint *.ts && npm run prettier:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 122 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [TrustWallet/trust-ray](https://github.com/TrustWallet/trust-ray) | 121 | `cross-env NODE_ENV=test mocha --recursive --require ts-node/register 'test/**/*.test.ts' --exit` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 120 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 120 | `istanbul test -- _mocha` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 119 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 119 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 118 | `mocha --timeout 10000` | 
| [DotJoshJohnson/vscode-xml](https://github.com/DotJoshJohnson/vscode-xml) | 117 | `npm run compile && mocha ./out/test/**/*.js` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 117 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 116 | `mocha --require source-map-support/register dist/test` | 
| [VirgilSecurity/demo-twilio-chat-js](https://github.com/VirgilSecurity/demo-twilio-chat-js) | 114 | `mocha --timeout 5000 -r ts-node/register -r tsconfig-paths/register ./api/tests/*.test.ts` | 
| [prh/prh](https://github.com/prh/prh) | 114 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 114 | `mocha test` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 114 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 111 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 111 | `npm run-script build && mocha --opts test/mocha.opts build/test` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 110 | `gulp compile && mocha` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 109 | `mocha lib/test` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 106 | `mocha -R spec dist/test/**/*.js` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 106 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [gamestdio/colyseus.js](https://github.com/gamestdio/colyseus.js) | 106 | `mocha test/*.ts --require ts-node/register` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 104 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 103 | `cross-env NODE_ENV=test mocha --exit` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 104 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 103 | `cross-env NODE_ENV=test mocha --exit` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 102 | `mocha --full-trace tests/test.js` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 101 | `mocha` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 99 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 99 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 99 | `webpack && mocha-phantomjs test/index.html` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 96 | `tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 95 | `npm-run-all build test:mocha test:coverage lint` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 95 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 95 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 94 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 94 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 93 | `tsc; mocha --recursive test/suite/` | 
| [filestack/filestack-js](https://github.com/filestack/filestack-js) | 93 | `npm run build && concurrently -r --kill-others 'npm run prism:mock' 'npm run toxy' 'npm run lint && TEST_ENV=unit karma start && TEST_ENV=unit nyc mocha'` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 93 | `mocha ./spec/*.js` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 92 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 92 | `node node_modules/mocha/bin/mocha` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 91 | `mocha --compilers ts:ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 91 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 91 | `mocha` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 90 | `mocha --recursive -t 4000` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 90 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 90 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 89 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 89 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 89 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 88 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 88 | `mocha` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 88 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 87 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 87 | `mocha test/* --timeout 500000` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 86 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 86 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 86 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 86 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 86 | `cd test && mocha -r ts-node/register *.ts` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 85 | `mocha ./dist/test --recursive` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 85 | `mocha ./dist/test --recursive` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 85 | `mocha test/ --recursive` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 84 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 84 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register 'test/**/*.ts'` | 
| [MichaelSolati/geofirestore](https://github.com/MichaelSolati/geofirestore) | 83 | `nyc --reporter=html --reporter=text mocha` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 82 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 81 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [nicksenger/react-arcgis](https://github.com/nicksenger/react-arcgis) | 81 | `nyc mocha` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 81 | `mocha` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 80 | `nyc npm run _mocha` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 80 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 76 | `npm run lint && npm run prettier && npm run mocha` | 
| [dsherret/ts-nameof](https://github.com/dsherret/ts-nameof) | 76 | `npm run --silent copy-test-files && nyc --reporter=lcov mocha --opts mocha.opts` | 
| [teambition/ReactiveDB](https://github.com/teambition/ReactiveDB) | 74 | `npm run lint && NODE_ENV=test tman --mocha spec-js/test/run.js` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 74 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [AlexGalays/spacelift](https://github.com/AlexGalays/spacelift) | 74 | `mocha test/test.js && mocha --ui tdd test/option.js && mocha --ui tdd test/result.js` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 74 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 73 | `mocha --compilers js:babel-core/register --recursive` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 73 | `mocha --require ts-node/register test/**/*.ts` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 72 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 71 | `nyc mocha --recursive test/**/*.ts` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 71 | `nyc mocha --require espower-typescript/guess --require source-map-support/register "test/**/*.test.ts"` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 70 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 70 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 69 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 68 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 68 | `npm run lint && nyc mocha` | 
| [httptoolkit/mockttp](https://github.com/httptoolkit/mockttp) | 68 | `npm run build && npm run test:mocha && npm run test:browser` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 67 | `mocha --ui tdd out/test/extension.test.js` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 67 | `mocha` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 66 | `mocha -r ts-node/register test/*.ts` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 65 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 64 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [PeculiarVentures/graphene](https://github.com/PeculiarVentures/graphene) | 64 | `mocha` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 64 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 64 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 64 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 64 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [wonderful-panda/vue-tsx-support](https://github.com/wonderful-panda/vue-tsx-support) | 63 | `npm-run-all prettier tsc-test mocha` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 63 | `npm run compile && mocha && npm run lint` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 63 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 62 | `npm run lint && npm run mocha` | 
| [wix/rawss](https://github.com/wix/rawss) | 62 | `mocha` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 62 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 62 | `mocha out/**/*.spec.js` | 
| [AugurProject/augur-node](https://github.com/AugurProject/augur-node) | 62 | `mocha test/unit` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 62 | `mocha -r ts-node/register 'test/main.js'` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 61 | `mocha -u tdd ./out/tests/` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 61 | `mocha 'lib/**/__tests__/*.js'` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 61 | `mocha dist/test/*.js` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 60 | `TS_NODE_FILES=true mocha --timeout 20000 --slow 6000 --require ts-node/register "src/test/test*.ts"` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 59 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 59 | `tsc && mocha "dist/test/**/*.js" ` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 59 | `mocha build/test` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 59 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 58 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 58 | `nyc mocha lib/**/*Test.js` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 57 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 57 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 56 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 56 | `nyc mocha` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 56 | `nyc mocha` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 55 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [puzzle-js/PuzzleJs](https://github.com/puzzle-js/PuzzleJs) | 54 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 54 | `mocha` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 54 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 54 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 53 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 53 | `npm run build && npm run mocha` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 53 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 53 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 52 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 52 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 52 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 52 | `mocha --recursive` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 52 | `nyc mocha build/test` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 52 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 51 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 51 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 51 | `nyc mocha --opts .mocha.opts` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 50 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 50 | `NODE_ENV=test nyc mocha` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 50 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 50 | `mocha build/tests/index.js` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 50 | `mocha --timeout 30000 test/**/*.js` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 50 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 49 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [DhyanaChina/todo-live](https://github.com/DhyanaChina/todo-live) | 49 | `mocha` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 48 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 48 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 48 | `mocha -r ./src/test/common/setup.ts ./lib/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 48 | `NODE_ENV=test nyc mocha` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 48 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 48 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 48 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 48 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd ./out/test/extension.test.js` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 47 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 47 | `mocha --compilers ts:ts-node/register --recursive` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 47 | `node_modules/.bin/istanbul cover node_modules/.bin/_mocha -- --bail --check-leaks dist/test` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 47 | `mocha .tmp/test/**/*.spec.js` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 47 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 46 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [indutny/llparse](https://github.com/indutny/llparse) | 46 | `npm run mocha && npm run lint` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 46 | `mocha --timeout 10000 --slow 2500 tests/all-test-cases.js` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 46 | `npm run lint && npm run mocha` | 
| [steven-xie/express-starter](https://github.com/steven-xie/express-starter) | 46 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 45 | `mocha` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 45 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 44 | `mocha --opts config/mocha.opts` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 44 | `tsc --version && tsc && mocha out/test` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 44 | `mocha -R spec ./test` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 44 | `mocha .tmp/spec/index.spec.js` | 
| [SPGoding/spu](https://github.com/SPGoding/spu) | 44 | `mocha --require espower-typescript/guess "./src/tests/**/*.ts"` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 44 | `nyc mocha --opts test/mocha.opts` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 43 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 43 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [balmbees/dynamo-typeorm](https://github.com/balmbees/dynamo-typeorm) | 43 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 42 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [DhyanaChina/koa2-typescript-guide](https://github.com/DhyanaChina/koa2-typescript-guide) | 42 | `mocha` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 42 | `mocha out/{,**/}*.spec.js -s 0` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 42 | `npm run compile && mocha && npm run lint` | 
| [zswang/icity](https://github.com/zswang/icity) | 42 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 42 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 41 | `mocha --ui qunit` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 41 | `cross-env NODE_ENV=test mocha` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 41 | `npm run lint && mocha dist/spec` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 41 | `npm run compile && mocha` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 41 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [indutny/llhttp](https://github.com/indutny/llhttp) | 41 | `npm run mocha && npm run lint` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 41 | `mocha test` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 41 | `tsc && mocha build/test` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 40 | `mocha --opts mocha.opts --watch` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 40 | `node_modules/.bin/mocha` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 40 | `mocha --opts spec/mocha.opts spec/**/*-spec.ts` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 40 | `mocha && npm run aplus` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 40 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 39 | `mocha` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 39 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 39 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 39 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 39 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 39 | `mocha out/test` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 39 | `nyc mocha` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 39 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 39 | `mocha ./dist/es6/test -R spec --recursive --timeout 30000` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 39 | `mocha index.test.js` | 
| [webix-hub/webix-jet](https://github.com/webix-hub/webix-jet) | 39 | `webpack && phantomjs node_modules/mocha-phantomjs-core/mocha-phantomjs-core.js tests/index.html spec` | 
| [aurelia/bundler](https://github.com/aurelia/bundler) | 39 | `mocha --reporter spec --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 39 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 38 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 38 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 38 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 38 | `node_modules/.bin/mocha --watch` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 38 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 38 | `mocha --require ts-node/register tests/**/*.ts` | 
| [willryan/factory.ts](https://github.com/willryan/factory.ts) | 38 | `NODE_ENV=test mocha --require spec/setup.js --require ts-node/register` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 38 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 38 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 38 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 37 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 37 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 37 | `tsc && mocha dist/**/*.spec.js` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 37 | `mocha --opts test/mocha.opts` | 
| [utopian-io/api.utopian.io](https://github.com/utopian-io/api.utopian.io) | 37 | `cross-env NODE_ENV=test npx mocha --ui bdd --reporter spec --colors --recursive -r ts-node/register tests/index.ts` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 37 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 37 | `nyc mocha --require source-map-support/register --require ts-node/register test/**/*.ts` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 37 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 36 | `mocha --opts cli-test-mocha.opts` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 36 | `tsc && npm run lint && mocha` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 36 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [Polymer/polymer-linter](https://github.com/Polymer/polymer-linter) | 36 | `npm run build && mocha && npm run lint` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 36 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 36 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 35 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [fyndme/messenger-bot-tester](https://github.com/fyndme/messenger-bot-tester) | 35 | `mocha ./test-build` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 35 | `mocha` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 34 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 34 | `mocha test/*.js` | 
| [Draccoz/twc](https://github.com/Draccoz/twc) | 34 | `npm run lint && mocha --require ts-node/register --ui bdd tests/tests.spec.ts` | 
| [davetemplin/web-request](https://github.com/davetemplin/web-request) | 34 | `mocha` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 34 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 34 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [forthright/vile](https://github.com/forthright/vile) | 34 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [paralin/grpc-bus](https://github.com/paralin/grpc-bus) | 34 | `npm run lint && npm run mocha` | 
| [qtumproject/qtumjs](https://github.com/qtumproject/qtumjs) | 34 | `mocha  lib/*_test.js` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 33 | `mocha --opts ./mocha.opts` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 33 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 33 | `npm run prettier && npm run lint && npm run mocha` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 33 | `mocha --opts ./mocha.opts` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 33 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 33 | `npm run prettier && npm run lint && npm run mocha` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 33 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [userpixel/typescript](https://github.com/userpixel/typescript) | 33 | `mocha test` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 33 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [tgreyjs/typedoc-plugin-markdown](https://github.com/tgreyjs/typedoc-plugin-markdown) | 33 | `mocha test/test.js` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 33 | `mocha --reporter spec` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 33 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [infinum/mobx-collection-store](https://github.com/infinum/mobx-collection-store) | 33 | `NODE_ENV=test nyc mocha` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 33 | `npm run mocha && npm run lint` | 
| [supergraphql/supergraph](https://github.com/supergraphql/supergraph) | 33 | `nyc mocha ./dist/**/*.spec.js` | 
| [mixi-inc/css-semdiff](https://github.com/mixi-inc/css-semdiff) | 32 | `mocha --opts mocha.opts './dist/**/*.test.js'` | 
| [agea/CmisJS](https://github.com/agea/CmisJS) | 32 | `tsc && mocha dist/**/*.spec.js` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 32 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 32 | `mocha --recursive` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 32 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [igorzg/typeix](https://github.com/igorzg/typeix) | 32 | `npm run compile && mocha build/tests/ --debug --full-trace` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 32 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [GoodgameStudios/RobotlegsJS](https://github.com/GoodgameStudios/RobotlegsJS) | 32 | `nyc mocha` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 32 | `tsc && mocha spec/` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 31 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [ForbesLindesay/barrage](https://github.com/ForbesLindesay/barrage) | 31 | `mocha -R spec lib/test.js` | 
| [davetemplin/async-parallel](https://github.com/davetemplin/async-parallel) | 31 | `mocha` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 31 | `cross-env NODE_ENV=test nyc mocha test/**/*.ts` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 31 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [haoliangyu/boundary.now](https://github.com/haoliangyu/boundary.now) | 31 | `mocha test/**/*.test.ts --require ts-node/register --require reflect-metadata` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 31 | `mocha --recursive "dist/**/*.test.js"` | 
| [mrmlnc/vscode-stylefmt](https://github.com/mrmlnc/vscode-stylefmt) | 30 | `mocha out/**/*.spec.js -s 0` | 
| [tsframework/ts-framework](https://github.com/tsframework/ts-framework) | 30 | `mocha build-test --recursive` | 
| [NikitchenkoSergey/scheme-designer](https://github.com/NikitchenkoSergey/scheme-designer) | 30 | `mocha` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 30 | `mocha` | 
| [mulesoft-labs/yaml-ast-parser](https://github.com/mulesoft-labs/yaml-ast-parser) | 30 | `npm run build && mocha --ui tdd dist/test` | 
| [siegebell/vsc-prettify-symbols-mode](https://github.com/siegebell/vsc-prettify-symbols-mode) | 30 | `tsc -p ./ && mocha -u tdd ./out/test` | 
| [Rich-Harris/port-authority](https://github.com/Rich-Harris/port-authority) | 30 | `mocha --opts mocha.opts` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 29 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [gwuhaolin/spring-data-rest-js](https://github.com/gwuhaolin/spring-data-rest-js) | 29 | `tsc & mocha` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 29 | `mocha` | 
| [evebook/api](https://github.com/evebook/api) | 29 | `nyc --require ts-node/register mocha src/**/*.spec.ts --reporter spec` | 
| [creeperyang/id3-parser](https://github.com/creeperyang/id3-parser) | 29 | `TS_NODE_PROJECT='test/tsconfig.json' mocha --require ts-node/register 'test/*.spec.ts' --reporter dot` | 
| [rhysd/electron-in-page-search](https://github.com/rhysd/electron-in-page-search) | 29 | `electron-mocha --timeout 10000 --renderer test/*.js` | 
| [nicolastakashi/linq-to-type](https://github.com/nicolastakashi/linq-to-type) | 29 | `nyc mocha` | 
| [leizongmin/leizm-web](https://github.com/leizongmin/leizm-web) | 29 | `npm run format && mocha --require ts-node/register --exit "src/test/**/*.ts"` | 
| [nilobarp/text2json](https://github.com/nilobarp/text2json) | 29 | `DEBUG=TP* mocha dist/test/spectrum-tests.js` | 
| [ShieldBattery/node-interval-tree](https://github.com/ShieldBattery/node-interval-tree) | 29 | `mocha -R spec --compilers ts:ts-node/register test/*.ts` | 
| [palmerabollo/bingspeech-api-client](https://github.com/palmerabollo/bingspeech-api-client) | 29 | `npm run build && mocha -R spec 'lib/**/*.spec.js'` | 
| [NE-LOAN-FED/NE-Component](https://github.com/NE-LOAN-FED/NE-Component) | 29 | `mocha --compilers js:babel-register --recursive` | 
| [coderfox/clover](https://github.com/coderfox/clover) | 29 | `nyc mocha` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 29 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [patrimart/monadness-js](https://github.com/patrimart/monadness-js) | 29 | `./node_modules/.bin/istanbul cover ./node_modules/mocha/bin/_mocha --report lcovonly -- -R spec && cat ./coverage/lcov.info | ./node_modules/coveralls/bin/coveralls.js && rm -rf ./coverage` | 
| [secret-tech/backend-token-wallets](https://github.com/secret-tech/backend-token-wallets) | 29 | `mocha -r ts-node/register -r test/prepare.ts src/**/*.spec.ts` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 28 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [codefoster/waterrower](https://github.com/codefoster/waterrower) | 28 | `mocha test` | 
| [bespoken/virtual-device-sdk](https://github.com/bespoken/virtual-device-sdk) | 28 | `nyc mocha lib/test/*Test.js` | 
| [ERCdEX/automation-toolkit](https://github.com/ERCdEX/automation-toolkit) | 28 | `rm -rf ./test-data && NODE_ENV=test mocha -t 15000 -r ts-node/register src/**/*.spec.ts` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 28 | `tsc -p .tsconfig.test.json && mocha` | 
| [3VLINC/graphql-to-typescript](https://github.com/3VLINC/graphql-to-typescript) | 28 | `mocha "dist/**/*.test.js"` | 
| [tbluemel/rtf.js](https://github.com/tbluemel/rtf.js) | 28 | `mocha test/test.js` | 
| [georgehanson/Vue-Form-Components](https://github.com/georgehanson/Vue-Form-Components) | 28 | `mocha-webpack --webpack-config="webpack.test.config.js" --require="tests/setup.ts" tests/**/*.spec.ts` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 28 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [VaclavObornik/di-ts](https://github.com/VaclavObornik/di-ts) | 28 | `node ./node_modules/mocha/bin/mocha ./spec/ --recursive --require reflect-metadata` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 28 | `nyc mocha` | 
| [mseemann/js-restful-express](https://github.com/mseemann/js-restful-express) | 27 | `istanbul cover node_modules/mocha/bin/_mocha --report lcov -x '*.spec.*'  -- -c --check-leaks --require ts-node/register --require core-js --recursive --reporter spec src/**/*.spec.ts` | 
| [Azure/oav](https://github.com/Azure/oav) | 27 | `npm run tsc && npm run tslint && nyc mocha ./test/**/*.ts -r ts-node/register -t 10000` | 
| [AsynkronIT/protoactor-js](https://github.com/AsynkronIT/protoactor-js) | 27 | `mocha --opts test/mocha.opts -w` | 
| [cartant/firebase-nightlight](https://github.com/cartant/firebase-nightlight) | 27 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [lazerwalker/storyboard](https://github.com/lazerwalker/storyboard) | 27 | `mocha-webpack tests` | 
| [exercism/typescript](https://github.com/exercism/typescript) | 27 | `mocha test` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 27 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [ClickerMonkey/vuex-router-actions](https://github.com/ClickerMonkey/vuex-router-actions) | 27 | `mocha -r ts-node/register tests/**/*.ts` | 
| [masvis/angular4-hal](https://github.com/masvis/angular4-hal) | 27 | `mocha -r ts-node/register --config=test/test-config.json test/*.test.ts` | 
| [vrudikov/typescript-rest-boilerplate](https://github.com/vrudikov/typescript-rest-boilerplate) | 27 | `cross-env NODE_ENV=test mocha` | 
| [alexeagle/tsetse](https://github.com/alexeagle/tsetse) | 26 | `tsc && mocha built/test/*.js` | 
| [sebsylvester/botbuilder-wit](https://github.com/sebsylvester/botbuilder-wit) | 26 | `nyc --reporter=lcov mocha` | 
| [glixlur/jsx-dom](https://github.com/glixlur/jsx-dom) | 26 | `nyc --reporter=html mocha ./test/test.tsx --require ts-node/register` | 
| [tipether/tipether](https://github.com/tipether/tipether) | 26 | `mocha --require ts-node/register test/**/*.ts` | 
| [larshp/abaplint](https://github.com/larshp/abaplint) | 26 | `mocha --recursive --reporter progress build/test` | 
| [alexanderwe/checksum-validator](https://github.com/alexanderwe/checksum-validator) | 26 | `mocha` | 
| [tusharmath/observable-air](https://github.com/tusharmath/observable-air) | 26 | `tsc && mocha --reporter=min` | 
| [fsahmad/typescript-uml](https://github.com/fsahmad/typescript-uml) | 26 | `npm run build && mocha --compilers ts:ts-node/register --recursive 'src/**/*-spec.ts'` | 
| [RxParse/Parse-SDK-ts](https://github.com/RxParse/Parse-SDK-ts) | 26 | `node out/test/utils/init.js && mocha --timeout 30000 $(find out/test -name '*.js')` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 26 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 26 | `mocha test/unit` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 26 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [alitaheri/jss-rtl](https://github.com/alitaheri/jss-rtl) | 26 | `mocha --require ts-node/register "src/**/*.spec.ts"` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 26 | `atool-test-mocha ./src/**/*-test.js` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 26 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [TomShacham/http4js](https://github.com/TomShacham/http4js) | 26 | `tsc; mocha --require ts-node/register 'src/{test,ssl}/**/*.ts'` | 
| [ActionableAgile/jira-to-analytics](https://github.com/ActionableAgile/jira-to-analytics) | 25 | `mocha --opts mocha.opts` | 
| [sidewalklabs/totx](https://github.com/sidewalklabs/totx) | 25 | `mocha --compilers ts:ts-node/register **/*_test.ts` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 25 | `mocha` | 
| [funkia/io](https://github.com/funkia/io) | 25 | `nyc mocha --recursive test/**/*.ts` | 
| [windwp/vscode-expand-region](https://github.com/windwp/vscode-expand-region) | 25 | `mocha --ui tdd --recursive "out/**/*.test.js"` | 
| [tomitrescak/apollo-modules](https://github.com/tomitrescak/apollo-modules) | 25 | `mocha --report lcovonly src/*spec.ts --compilers ts:ts-node/register --bail` | 
| [nemtech/nem2-sdk-typescript-javascript](https://github.com/nemtech/nem2-sdk-typescript-javascript) | 25 | `mocha --ui bdd --recursive ./dist/test --timeout 90000` | 
| [PeculiarVentures/2key-ratchet](https://github.com/PeculiarVentures/2key-ratchet) | 25 | `mocha` | 
| [vincentdchan/MDE](https://github.com/vincentdchan/MDE) | 25 | `mocha ./build/test --harmony` | 
| [konvajs/ng2-konva](https://github.com/konvajs/ng2-konva) | 24 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 