# Find Repos in TypeScript Tested using Mocha

The list was updated at 01:55:11 11/04/18 PDT

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 63265 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 15571 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 9778 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 8969 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [sveltejs/svelte](https://github.com/sveltejs/svelte) | 8257 | `mocha --opts mocha.opts` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 6896 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 5980 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 5030 | `npm run mocha` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4474 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4146 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3337 | `mocha --opts mocha.opts` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 2814 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2778 | `mocha` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2528 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2412 | `mocha 'test/**/*.ts'` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 2324 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2098 | `mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1832 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1799 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1791 | `mocha` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1693 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [burtonator/polar-bookshelf](https://github.com/burtonator/polar-bookshelf) | 1461 | `find web/js -name '*Test.js' | xargs mocha-parallel-tests --timeout 10000 --max-parallel=1 --exit` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1361 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1316 | `nyc -x '' mocha` | 
| [gamestdio/colyseus](https://github.com/gamestdio/colyseus) | 1253 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1232 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [funkia/list](https://github.com/funkia/list) | 1192 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1149 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1145 | `mocha --opts mocha.opts` | 
| [watson-developer-cloud/node-sdk](https://github.com/watson-developer-cloud/node-sdk) | 1139 | `nyc mocha test/unit/ test/integration/ && nyc report --reporter=html` | 
| [shanalikhan/code-settings-sync](https://github.com/shanalikhan/code-settings-sync) | 1097 | `npm run vscode:prepublish && node ./node_modules/bin/mocha --recursive` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 1077 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1076 | `nyc --reporter=html --reporter=text mocha` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1074 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 1009 | `tsc -p ./ && mocha` | 
| [google/clasp](https://github.com/google/clasp) | 960 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [itchio/itch](https://github.com/itchio/itch) | 936 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 916 | `mocha --opts test/mocha.opts` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 876 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 812 | `mocha bin/tests/test.js` | 
| [netgusto/nodebook](https://github.com/netgusto/nodebook) | 748 | `mocha test/backend` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 723 | `yarn run lint && yarn run test:mocha` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 708 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 680 | `mocha` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 676 | `mocha --compilers ts:ts-node/register test/*.js || true` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 674 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 647 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 647 | `mocha --recursive` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 637 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 637 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 601 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 586 | `npm run lint && npm run mocha` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 582 | `mocha "out/**/*.spec.js" -s 0` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 563 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 547 | `mocha` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 539 | `mocha test` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 538 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 534 | `mocha --opts test/mocha.opts dist/test` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 524 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 518 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 514 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 498 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 496 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 476 | `mocha --opts mocha.opts` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 462 | `npm run build && mocha` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 454 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 443 | `mocha --opts mocha.opts` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 441 | `_mocha --` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 432 | `npm run mocha` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 426 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 421 | `cross-env NODE_ENV=test mocha **/*.spec.ts --compilers ts:ts-node/register` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 419 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [dsherret/ts-simple-ast](https://github.com/dsherret/ts-simple-ast) | 415 | `cross-env TS_NODE_COMPILER="ttypescript" TS_NODE_TRANSPILE_ONLY="true" mocha --opts mocha.opts` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 408 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [Romakita/ts-express-decorators](https://github.com/Romakita/ts-express-decorators) | 408 | `npm run clean && npm run tsc && npm run tslint && cross-env NODE_ENV=test nyc --reporter=html --reporter=text _mocha --recursive` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 401 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 391 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 384 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 383 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 375 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 371 | `cd test && mocha -r ts-node/register *.ts` | 
| [jacobbogers/libRmath.js](https://github.com/jacobbogers/libRmath.js) | 365 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 359 | `mocha` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 348 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 343 | `npm run build && mocha` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 328 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 325 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 305 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 302 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [Microsoft/node-pty](https://github.com/Microsoft/node-pty) | 291 | `cross-env NODE_ENV=test mocha -R spec --exit lib/*.test.js` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 290 | `mocha` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 288 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 280 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 274 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 272 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 270 | `mocha --compilers js:babel-register test/**/*.js` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 269 | `mocha` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 269 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 266 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 266 | `mocha lib/test` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 264 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 259 | `mocha test` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 256 | `mocha src/**/*.spec.ts` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 248 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 247 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts view/test/test-heightmap.ts` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 246 | `mocha` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 241 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 233 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 231 | `tsc && mocha` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 226 | `tsc && mocha dist/**/*.spec.js` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 225 | `nyc --reporter html mocha` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 224 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [dubzzz/fast-check](https://github.com/dubzzz/fast-check) | 218 | `npm run build && nyc mocha "test/unit/**/*.spec.ts"` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 215 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 207 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 206 | `mocha test` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 200 | `mocha -R spec test/integration` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 198 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 197 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [ClickSimply/Nano-SQL](https://github.com/ClickSimply/Nano-SQL) | 196 | `mocha -r ts-node/register tests/index.ts` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 196 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 196 | `mocha dist/test.js` | 
| [Zarel/Pokemon-Showdown-Client](https://github.com/Zarel/Pokemon-Showdown-Client) | 195 | `eslint --config=.eslintrc.js --cache --cache-file=eslint-cache/base js/ && eslint --config=build-tools/.eslintrc.js --cache --cache-file=eslint-cache/build build-tools/update build-tools/build-indexes && tsc && node build && mocha` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 193 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 188 | `mocha-webpack "src/**/*.ts"` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 188 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 188 | `cross-env NODE_ENV=test mocha` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 186 | `mocha js` | 
| [jacobbogers/blasjs](https://github.com/jacobbogers/blasjs) | 184 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 184 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 180 | `mocha "test/**/*.spec.ts"` | 
| [bmewburn/intelephense](https://github.com/bmewburn/intelephense) | 179 | `mocha -r ts-node/register test/*.ts` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 177 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [AmirTugi/tea-school](https://github.com/AmirTugi/tea-school) | 176 | `npx ts-mocha ./src/tests/**.ts` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 173 | `nyc mocha --recursive test/**/*.ts` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 172 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 171 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 170 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 170 | `npm run lint && npm run mocha` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 167 | `npm run clean && npm run build && npm run lint && mocha` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 167 | `npm run build && npm run mocha` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 166 | `mocha lib/spec/core` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 164 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [square/babel-codemod](https://github.com/square/babel-codemod) | 159 | `mocha "test/**/*Test.js"` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 158 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 156 | `tsc && cd dist && mocha` | 
| [Chinachu/Mirakurun](https://github.com/Chinachu/Mirakurun) | 153 | `mocha --exit test/*.spec.js` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 153 | `gulp compile && mocha --timeout 10000 -u tdd ./out/tests/` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 153 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [emmanueltouzery/prelude.ts](https://github.com/emmanueltouzery/prelude.ts) | 148 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 147 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [calidion/vig](https://github.com/calidion/vig) | 145 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 141 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 137 | `tsc && mocha` | 
| [hydux/hydux](https://github.com/hydux/hydux) | 136 | `npm run mocha -- "src/test/unit/*.test.ts"` | 
| [Azure/azure-functions-pack](https://github.com/Azure/azure-functions-pack) | 135 | `npm run build && mocha --compilers ts:ts-node/register --recursive test/**/*-spec.ts` | 
| [kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | 134 | `nyc mocha` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 132 | `mocha -r ts-node/register test/*.ts` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 132 | `mocha` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 131 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 131 | `mocha test/unit/ --exit` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 131 | `TEST_BROWSER_DRIVER=phantomjs meteor test --driver-package=ardatan:mocha` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 131 | `mocha lib/test` | 
| [nspragg/filehound](https://github.com/nspragg/filehound) | 129 | `mocha -r ts-node/register test/*.ts` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 128 | `mocha --require ts-node/register test/**/*.ts` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 128 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 127 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [TrustWallet/trust-ray](https://github.com/TrustWallet/trust-ray) | 125 | `cross-env NODE_ENV=test mocha --recursive --require ts-node/register 'test/**/*.test.ts' --exit` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 125 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 125 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [DotJoshJohnson/vscode-xml](https://github.com/DotJoshJohnson/vscode-xml) | 124 | `npm run compile && mocha ./out/test/**/*.js` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 123 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 123 | `cd test && mocha -r ts-node/register *.ts` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 122 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 122 | `gulp compile && mocha` | 
| [cartant/rxjs-marbles](https://github.com/cartant/rxjs-marbles) | 121 | `yarn run lint && yarn run test:build && cross-env FAILING=0 yarn run test:ava && cross-env FAILING=0 yarn run test:jasmine && cross-env FAILING=0 yarn run test:jasmine-angular && cross-env FAILING=0 yarn run test:jest && cross-env FAILING=0 yarn run test:mocha && cross-env FAILING=0 yarn run test:tape` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 121 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 121 | `istanbul test -- _mocha` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 121 | `mocha --require source-map-support/register dist/test` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 120 | `mocha --timeout 10000` | 
| [prh/prh](https://github.com/prh/prh) | 119 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 118 | `mocha test` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 118 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 118 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 117 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 117 | `npm run-script build && mocha --opts test/mocha.opts build/test` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 114 | `mocha` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 113 | `cross-env NODE_ENV=test mocha --exit` | 
| [VirgilSecurity/demo-twilio-chat-js](https://github.com/VirgilSecurity/demo-twilio-chat-js) | 112 | `mocha --timeout 5000 -r ts-node/register -r tsconfig-paths/register ./api/tests/*.test.ts` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 112 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [gamestdio/colyseus.js](https://github.com/gamestdio/colyseus.js) | 111 | `mocha test/*.ts --require ts-node/register` | 
| [Soluto/graphql-to-mongodb](https://github.com/Soluto/graphql-to-mongodb) | 110 | `ts-mocha tests/**/*.spec.ts` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 110 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 108 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 108 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 108 | `nyc --reporter=html --reporter=text mocha` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 107 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 106 | `mocha -R spec dist/test/**/*.js` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 104 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 104 | `mocha --full-trace tests/test.js` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 103 | `webpack && mocha-phantomjs test/index.html` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 100 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 100 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 99 | `mocha --recursive -t 4000` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 99 | `mocha` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 98 | `npm-run-all build test:mocha test:coverage lint` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 98 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 98 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 97 | `tsc; mocha --recursive lib/ test/runner` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 97 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 97 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 96 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 95 | `mocha --compilers ts:ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 95 | `mocha ./spec/*.js` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 95 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 95 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 94 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 94 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 93 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 93 | `mocha` | 
| [wildbit/postmark.js](https://github.com/wildbit/postmark.js) | 93 | `node_modules/mocha/bin/mocha --timeout 10000 --retries 1 -r ts-node/register test/**/*test.ts` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 93 | `node node_modules/mocha/bin/mocha` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 92 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 92 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [nicksenger/react-arcgis](https://github.com/nicksenger/react-arcgis) | 92 | `nyc mocha` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 91 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 90 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 90 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [nucleojs/nucleo](https://github.com/nucleojs/nucleo) | 90 | `mocha -r ts-node/register` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 90 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 89 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 88 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 88 | `mocha test/ --recursive` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 88 | `nyc mocha --require espower-typescript/guess --require source-map-support/register "test/**/*.test.ts"` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 88 | `mocha test/* --timeout 500000` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 87 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register 'test/**/*.ts'` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 87 | `npm run lint && npm run prettier && npm run mocha` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 86 | `mocha ./dist/test --recursive` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 86 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [dsherret/ts-nameof](https://github.com/dsherret/ts-nameof) | 86 | `yarn run --silent copy-test-files && nyc --reporter=lcov mocha --opts mocha.opts` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 86 | `mocha` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 84 | `nyc npm run _mocha` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 84 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 84 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 83 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 80 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 79 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [AlexGalays/spacelift](https://github.com/AlexGalays/spacelift) | 78 | `mocha test/test.js && mocha --ui tdd test/option.js && mocha --ui tdd test/result.js` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 78 | `mocha` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 77 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 76 | `mocha --require ts-node/register test/**/*.ts` | 
| [teambition/ReactiveDB](https://github.com/teambition/ReactiveDB) | 75 | `npm run lint && NODE_ENV=test tman --mocha spec-js/test/run.js` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 74 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 74 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 74 | `mocha --ui tdd out/test/extension.test.js` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 73 | `nyc mocha --recursive test/**/*.ts` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 73 | `mocha --compilers js:babel-core/register --recursive` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 73 | `npm run lint && nyc mocha` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 72 | `npm run lint && npm run mocha` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 72 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 72 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 72 | `mocha dist/test` | 
| [httptoolkit/mockttp](https://github.com/httptoolkit/mockttp) | 71 | `npm run build && npm run test:mocha && npm run test:browser` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 70 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 70 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 70 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 68 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 67 | `mocha build/test` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 67 | `mocha -r ts-node/register 'test/main.js'` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 67 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 66 | `tsc && mocha "dist/test/**/*.js" ` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 66 | `mocha -r ./src/test/common/setup.ts ./lib/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 66 | `mocha -r ts-node/register test/*.ts` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 65 | `mocha -u tdd ./out/tests/` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 65 | `npm run compile && mocha && npm run lint` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 65 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 64 | `nyc mocha` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 64 | `mocha out/**/*.spec.js` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 64 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 63 | `nyc mocha lib/**/*Test.js` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 63 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 62 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 62 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 62 | `TS_NODE_FILES=true mocha --opts src/test/mocha.opts "src/test/test*.ts"` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 62 | `mocha 'lib/**/__tests__/*.js'` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 61 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 61 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 61 | `mocha dist/test/*.js` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 60 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 60 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [wix/rawss](https://github.com/wix/rawss) | 60 | `mocha` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 60 | `nyc mocha` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 59 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 58 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 57 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 57 | `mocha build/tests/index.js` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 57 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 57 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 57 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [puzzle-js/PuzzleJs](https://github.com/puzzle-js/PuzzleJs) | 56 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 56 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 56 | `nyc mocha build/test` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 55 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 55 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 54 | `npm run build && npm run mocha` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 54 | `mocha --timeout 30000 test/**/*.js` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 53 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 53 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 53 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 53 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 53 | `nyc mocha --opts .mocha.opts` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 53 | `mocha` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 53 | `mocha --recursive` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 53 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 53 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd ./out/test/extension.test.js` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 52 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 52 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 52 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 51 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 51 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 50 | `NODE_ENV=test nyc mocha` | 
| [indutny/llparse](https://github.com/indutny/llparse) | 50 | `npm run mocha && npm run lint` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 50 | `mocha --timeout 10000 --slow 2500 tests/all-test-cases.js` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 50 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [DhyanaChina/koa2-typescript-guide](https://github.com/DhyanaChina/koa2-typescript-guide) | 49 | `mocha` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 49 | `NODE_ENV=test nyc mocha` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [DhyanaChina/todo-live](https://github.com/DhyanaChina/todo-live) | 49 | `mocha` | 
| [mono/TsToCSharp](https://github.com/mono/TsToCSharp) | 49 | `npm run lint && mocha  ./dist/TsToCSharpTests.js` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 48 | `tsc --version && tsc && mocha out/test` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 48 | `mocha .tmp/spec/index.spec.js` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 48 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 47 | `mocha --ui qunit` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 47 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 47 | `mocha --opts spec/mocha.opts spec/**/*-spec.ts` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 47 | `mocha --compilers ts:ts-node/register --recursive` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 47 | `mocha` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 47 | `node_modules/.bin/nyc npm run mocha` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 47 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 46 | `mocha --opts config/mocha.opts` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 46 | `cross-env NODE_ENV=test mocha` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 45 | `mocha` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 45 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 45 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 45 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [CommandBlockLogic/spu](https://github.com/CommandBlockLogic/spu) | 45 | `mocha --require espower-typescript/guess "./src/test/**/*.ts"` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 45 | `nyc mocha --opts test/mocha.opts` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 44 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 44 | `npm run lint && mocha dist/spec` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 44 | `npm run compile && mocha && npm run lint` | 
| [sourcegraph/browser-extensions](https://github.com/sourcegraph/browser-extensions) | 44 | `mocha --require ts-node/register --watch --watch-extensions ts './src/**/*.test.ts?(x)'` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 44 | `nyc mocha` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 44 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 44 | `mocha -R spec ./test` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 44 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 44 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [balmbees/dynamo-types](https://github.com/balmbees/dynamo-types) | 44 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 43 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 43 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 43 | `mocha --opts mocha.opts --watch` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 43 | `node_modules/.bin/mocha --watch` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 43 | `mocha --require ts-node/register tests/**/*.ts` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 43 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 43 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 43 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 42 | `npm run compile && mocha` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 42 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 42 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 42 | `mocha` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 42 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 42 | `mocha test` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 42 | `mocha index.test.js` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 42 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 41 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 41 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 41 | `mocha out/{,**/}*.spec.js -s 0` | 
| [indutny/llhttp](https://github.com/indutny/llhttp) | 41 | `npm run mocha && npm run lint` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 41 | `mocha --opts test/mocha.opts` | 
| [willryan/factory.ts](https://github.com/willryan/factory.ts) | 41 | `NODE_ENV=test mocha --require spec/setup.js --require ts-node/register` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 41 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 41 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 41 | `tsc && mocha build/test` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 40 | `node_modules/.bin/mocha` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 40 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 40 | `mocha && npm run aplus` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 40 | `mocha out/test` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 40 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 40 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 40 | `nyc mocha --require source-map-support/register --require ts-node/register test/**/*.ts` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 40 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 39 | `mocha --opts cli-test-mocha.opts` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 39 | `mocha test/*.js` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 39 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 39 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 39 | `mocha` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 39 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [webix-hub/webix-jet](https://github.com/webix-hub/webix-jet) | 39 | `webpack && phantomjs node_modules/mocha-phantomjs-core/mocha-phantomjs-core.js tests/index.html spec` | 
| [aurelia/bundler](https://github.com/aurelia/bundler) | 39 | `mocha --reporter spec --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 38 | `npm run prettier && npm run lint && npm run mocha` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 38 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 38 | `tsc && mocha dist/**/*.spec.js` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 38 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 37 | `tsc && npm run lint && mocha` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 37 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 37 | `tsc && npm run lint && mocha` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 37 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 37 | `nyc mocha build/test` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 37 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 37 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 37 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 37 | `mocha --reporter spec` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 37 | `nyc mocha` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 37 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 36 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 36 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [Polymer/polymer-linter](https://github.com/Polymer/polymer-linter) | 36 | `npm run build && mocha && npm run lint` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 36 | `mocha --recursive` | 
| [utopian-io/api.utopian.io](https://github.com/utopian-io/api.utopian.io) | 36 | `cross-env NODE_ENV=test npx mocha --ui bdd --reporter spec --colors --recursive -r ts-node/register tests/index.ts` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 36 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 35 | `mocha --opts ./mocha.opts` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 35 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [fyndme/messenger-bot-tester](https://github.com/fyndme/messenger-bot-tester) | 35 | `mocha ./test-build` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 35 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [evebook/api](https://github.com/evebook/api) | 35 | `nyc --require ts-node/register mocha src/**/*.spec.ts --reporter spec` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 35 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 35 | `cross-env NODE_ENV=test mocha test/**/*.ts` | 
| [infinum/mobx-collection-store](https://github.com/infinum/mobx-collection-store) | 35 | `NODE_ENV=test nyc mocha` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 34 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 34 | `mocha` | 
| [Microsoft/typescript-tslint-plugin](https://github.com/Microsoft/typescript-tslint-plugin) | 34 | `mocha ./out/**/*.test.js --slow 2000 --timeout 10000` | 
| [agea/CmisJS](https://github.com/agea/CmisJS) | 34 | `tsc && mocha dist/**/*.spec.js` | 
| [ethereum-ts/evm-ts](https://github.com/ethereum-ts/evm-ts) | 34 | `yarn lint && yarn test:mocha` | 
| [Draccoz/twc](https://github.com/Draccoz/twc) | 34 | `npm run lint && mocha --require ts-node/register --ui bdd tests/tests.spec.ts` | 
| [davetemplin/web-request](https://github.com/davetemplin/web-request) | 34 | `mocha` | 
| [forthright/vile](https://github.com/forthright/vile) | 34 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [paralin/grpc-bus](https://github.com/paralin/grpc-bus) | 34 | `npm run lint && npm run mocha` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 34 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [mixi-inc/css-semdiff](https://github.com/mixi-inc/css-semdiff) | 33 | `mocha --opts mocha.opts './dist/**/*.test.js'` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 33 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [userpixel/typescript](https://github.com/userpixel/typescript) | 33 | `mocha test` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 33 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [qtumproject/qtumjs](https://github.com/qtumproject/qtumjs) | 33 | `mocha  lib/*_test.js` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 33 | `npm run mocha && npm run lint` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 33 | `tsc && mocha spec/` | 
| [supergraphql/supergraph](https://github.com/supergraphql/supergraph) | 33 | `nyc mocha ./dist/**/*.spec.js` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 32 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [davetemplin/async-parallel](https://github.com/davetemplin/async-parallel) | 32 | `mocha` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 32 | `mocha test/*.spec.ts` | 
| [igorzg/typeix](https://github.com/igorzg/typeix) | 32 | `npm run compile && mocha build/tests/ --debug --full-trace` | 
| [GoodgameStudios/RobotlegsJS](https://github.com/GoodgameStudios/RobotlegsJS) | 32 | `nyc mocha` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 32 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [Rich-Harris/port-authority](https://github.com/Rich-Harris/port-authority) | 32 | `mocha --opts mocha.opts` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 31 | `mocha` | 
| [tsframework/ts-framework](https://github.com/tsframework/ts-framework) | 31 | `mocha build-test --recursive` | 
| [NikitchenkoSergey/scheme-designer](https://github.com/NikitchenkoSergey/scheme-designer) | 31 | `mocha` | 
| [ForbesLindesay/barrage](https://github.com/ForbesLindesay/barrage) | 31 | `mocha -R spec lib/test.js` | 
| [leizongmin/leizm-web](https://github.com/leizongmin/leizm-web) | 31 | `npm run format && mocha --require ts-node/register --exit "src/test/**/*.ts"` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 31 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [mulesoft-labs/yaml-ast-parser](https://github.com/mulesoft-labs/yaml-ast-parser) | 31 | `npm run build && mocha --ui tdd dist/test` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 31 | `tsc -p .tsconfig.test.json && mocha` | 
| [siegebell/vsc-prettify-symbols-mode](https://github.com/siegebell/vsc-prettify-symbols-mode) | 31 | `tsc -p ./ && mocha -u tdd ./out/test` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 31 | `mocha --recursive "dist/**/*.test.js"` | 
| [vrudikov/typescript-rest-boilerplate](https://github.com/vrudikov/typescript-rest-boilerplate) | 31 | `cross-env NODE_ENV=test mocha` | 
| [mrmlnc/vscode-stylefmt](https://github.com/mrmlnc/vscode-stylefmt) | 30 | `mocha out/**/*.spec.js -s 0` | 
| [rhysd/electron-in-page-search](https://github.com/rhysd/electron-in-page-search) | 30 | `electron-mocha --timeout 10000 --renderer test/*.js` | 
| [haoliangyu/boundary.now](https://github.com/haoliangyu/boundary.now) | 30 | `mocha test/**/*.test.ts --require ts-node/register --require reflect-metadata` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 30 | `mocha test/unit` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 30 | `atool-test-mocha ./src/**/*-test.js` | 
| [secret-tech/backend-token-wallets](https://github.com/secret-tech/backend-token-wallets) | 30 | `mocha -r ts-node/register -r test/prepare.ts src/**/*.spec.ts` | 
| [Azure/oav](https://github.com/Azure/oav) | 29 | `npm run tsc && npm run tslint && nyc mocha ./test/**/*.ts -r ts-node/register -t 10000 --reporter mocha-junit-reporter` | 
| [gwuhaolin/spring-data-rest-js](https://github.com/gwuhaolin/spring-data-rest-js) | 29 | `tsc & mocha` | 
| [creeperyang/id3-parser](https://github.com/creeperyang/id3-parser) | 29 | `TS_NODE_PROJECT='test/tsconfig.json' mocha --require ts-node/register 'test/*.spec.ts' --reporter dot` | 
| [acrazing/mobx-sync](https://github.com/acrazing/mobx-sync) | 29 | `mocha --require ts-node/register --slow 1000 ./src/**/*.spec.ts` | 
| [codefoster/waterrower](https://github.com/codefoster/waterrower) | 29 | `mocha test` | 
| [nicolastakashi/linq-to-type](https://github.com/nicolastakashi/linq-to-type) | 29 | `nyc mocha` | 
| [nilobarp/text2json](https://github.com/nilobarp/text2json) | 29 | `DEBUG=TP* mocha dist/test/spectrum-tests.js` | 
| [fsahmad/typescript-uml](https://github.com/fsahmad/typescript-uml) | 29 | `npm run build && mocha --compilers ts:ts-node/register --recursive 'src/**/*-spec.ts'` | 
| [googleapis/google-cloud-kvstore](https://github.com/googleapis/google-cloud-kvstore) | 29 | `nyc mocha build/test` | 
| [ShieldBattery/node-interval-tree](https://github.com/ShieldBattery/node-interval-tree) | 29 | `mocha -R spec --compilers ts:ts-node/register test/*.ts` | 
| [palmerabollo/bingspeech-api-client](https://github.com/palmerabollo/bingspeech-api-client) | 29 | `npm run build && mocha -R spec 'lib/**/*.spec.js'` | 
| [alitaheri/jss-rtl](https://github.com/alitaheri/jss-rtl) | 29 | `mocha --require ts-node/register "src/**/*.spec.ts"` | 
| [3VLINC/graphql-to-typescript](https://github.com/3VLINC/graphql-to-typescript) | 29 | `mocha "dist/**/*.test.js"` | 
| [coderfox/clover](https://github.com/coderfox/clover) | 29 | `nyc mocha` | 
| [tbluemel/rtf.js](https://github.com/tbluemel/rtf.js) | 29 | `mocha test/test.js` | 
| [georgehanson/Vue-Form-Components](https://github.com/georgehanson/Vue-Form-Components) | 29 | `mocha-webpack --webpack-config="webpack.test.config.js" --require="tests/setup.ts" tests/**/*.spec.ts` | 
| [masvis/angular4-hal](https://github.com/masvis/angular4-hal) | 29 | `mocha -r ts-node/register --config=test/test-config.json test/*.test.ts` | 
| [aleixmorgadas/nem-library-ts](https://github.com/aleixmorgadas/nem-library-ts) | 29 | `mocha --ui bdd --recursive ./dist/test ./dist/integration_test --timeout 60000` | 
| [patrimart/monadness-js](https://github.com/patrimart/monadness-js) | 29 | `./node_modules/.bin/istanbul cover ./node_modules/mocha/bin/_mocha --report lcovonly -- -R spec && cat ./coverage/lcov.info | ./node_modules/coveralls/bin/coveralls.js && rm -rf ./coverage` | 
| [mseemann/js-restful-express](https://github.com/mseemann/js-restful-express) | 28 | `istanbul cover node_modules/mocha/bin/_mocha --report lcov -x '*.spec.*'  -- -c --check-leaks --require ts-node/register --require core-js --recursive --reporter spec src/**/*.spec.ts` | 
| [glixlur/jsx-dom](https://github.com/glixlur/jsx-dom) | 28 | `nyc --reporter=html mocha test/test.tsx --require test/register` | 
| [jan-molak/tiny-types](https://github.com/jan-molak/tiny-types) | 28 | `nyc --report-dir ./reports/coverage mocha --opts ./mocha.opts 'spec/**/*.spec.*'` | 
| [larshp/abaplint](https://github.com/larshp/abaplint) | 28 | `mocha --recursive --reporter progress build/test` | 
| [exercism/typescript](https://github.com/exercism/typescript) | 28 | `mocha test` | 
| [nemtech/nem2-sdk-typescript-javascript](https://github.com/nemtech/nem2-sdk-typescript-javascript) | 28 | `mocha --ui bdd --recursive ./dist/test --timeout 90000` | 
| [bespoken/virtual-device-sdk](https://github.com/bespoken/virtual-device-sdk) | 28 | `nyc mocha lib/test/*Test.js` | 
| [googleapis/nodejs-logging-winston](https://github.com/googleapis/nodejs-logging-winston) | 28 | `mocha build/test` | 
| [ERCdEX/automation-toolkit](https://github.com/ERCdEX/automation-toolkit) | 28 | `rm -rf ./test-data && NODE_ENV=test mocha -t 15000 -r ts-node/register src/**/*.spec.ts` | 
| [NE-LOAN-FED/NE-Component](https://github.com/NE-LOAN-FED/NE-Component) | 28 | `mocha --compilers js:babel-register --recursive` | 
| [ste-vg/pop.svg](https://github.com/ste-vg/pop.svg) | 28 | `nyc mocha --require ./mocha.config.js -r ts-node/register 'src/**/*.spec.ts'  --exit --recursive --timeout 10000` | 
| [VaclavObornik/di-ts](https://github.com/VaclavObornik/di-ts) | 28 | `node ./node_modules/mocha/bin/mocha ./spec/ --recursive --require reflect-metadata` | 
| [TomShacham/http4js](https://github.com/TomShacham/http4js) | 28 | `tsc; mocha --require ts-node/register 'src/{test,ssl}/**/*.ts'` | 
| [AsynkronIT/protoactor-js](https://github.com/AsynkronIT/protoactor-js) | 27 | `mocha --opts test/mocha.opts -w` | 