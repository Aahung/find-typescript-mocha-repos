# Find Repos in TypeScript Tested using Mocha

The list was updated at 00:43:56 10/09/18 PDT

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 61233 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 15136 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 9239 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 8546 | `tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [sveltejs/svelte](https://github.com/sveltejs/svelte) | 8113 | `mocha --opts mocha.opts && agadoo shared.js` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 6824 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 5801 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 4863 | `npm run mocha` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4421 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4039 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3295 | `mocha --opts mocha.opts` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2752 | `mocha` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 2606 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2411 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2406 | `mocha 'test/**/*.ts'` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 2097 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2020 | `./node_modules/.bin/mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1803 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1790 | `mocha` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1748 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1669 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1333 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1276 | `nyc -x '' mocha` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1231 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [gamestdio/colyseus](https://github.com/gamestdio/colyseus) | 1194 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [funkia/list](https://github.com/funkia/list) | 1177 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1129 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [watson-developer-cloud/node-sdk](https://github.com/watson-developer-cloud/node-sdk) | 1120 | `nyc mocha test/unit/ test/integration/ && nyc report --reporter=html` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1103 | `mocha --opts mocha.opts` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1077 | `nyc --reporter=html --reporter=text mocha` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1048 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 990 | `tsc -p ./ && mocha` | 
| [itchio/itch](https://github.com/itchio/itch) | 919 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 908 | `mocha --opts test/mocha.opts` | 
| [google/clasp](https://github.com/google/clasp) | 875 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 870 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 848 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 763 | `mocha bin/tests/test.js` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 719 | `yarn run lint && yarn run test:mocha` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 704 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 670 | `mocha` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 658 | `mocha --compilers ts:ts-node/register test/*.js || true` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 648 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 644 | `mocha --recursive` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 633 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 628 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 620 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 598 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [burtonator/polar-bookshelf](https://github.com/burtonator/polar-bookshelf) | 597 | `mocha-parallel-tests --timeout 10000 --max-parallel=1 --exit --recursive web/js/**/*Test.js` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 586 | `npm run lint && npm run mocha` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 574 | `mocha "out/**/*.spec.js" -s 0` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 539 | `mocha` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 534 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 533 | `mocha --opts test/mocha.opts dist/test` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 523 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 523 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 516 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 512 | `mocha test` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 496 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 483 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 469 | `mocha --opts mocha.opts` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 464 | `npm run build && mocha` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 447 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 442 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 441 | `_mocha --` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 427 | `mocha --opts mocha.opts` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 421 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 417 | `npm run mocha` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 403 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 401 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 396 | `cross-env NODE_ENV=test mocha **/*.spec.ts --compilers ts:ts-node/register` | 
| [Romakita/ts-express-decorators](https://github.com/Romakita/ts-express-decorators) | 392 | `npm run clean && npm run tsc && npm run tslint && cross-env NODE_ENV=test nyc --reporter=html --reporter=text _mocha --recursive` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 390 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 390 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 383 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 380 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [dsherret/ts-simple-ast](https://github.com/dsherret/ts-simple-ast) | 371 | `cross-env TS_NODE_COMPILER="ttypescript" mocha --opts mocha.opts` | 
| [jacobbogers/libRmath.js](https://github.com/jacobbogers/libRmath.js) | 360 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 357 | `mocha` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 357 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 349 | `cd test && mocha -r ts-node/register *.ts` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 347 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 340 | `npm run build && mocha` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 320 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 320 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 294 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 291 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 289 | `mocha` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 279 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [Microsoft/node-pty](https://github.com/Microsoft/node-pty) | 276 | `cross-env NODE_ENV=test mocha -R spec --exit lib/*.test.js` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 274 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 270 | `mocha --compilers js:babel-register test/**/*.js` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 269 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 262 | `mocha` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 261 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 261 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 261 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 259 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 257 | `mocha lib/test` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 256 | `mocha src/**/*.spec.ts` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 249 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 240 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 231 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 231 | `tsc && mocha` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 229 | `mocha` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 226 | `nyc --reporter html mocha` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 224 | `mocha test` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 218 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts view/test/test-heightmap.ts` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 218 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts view/test/test-heightmap.ts` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 213 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 209 | `tsc && mocha dist/**/*.spec.js` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 208 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 205 | `mocha test` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 202 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 199 | `mocha -R spec test/integration` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 197 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 193 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 193 | `mocha dist/test.js` | 
| [dubzzz/fast-check](https://github.com/dubzzz/fast-check) | 187 | `npm run build && nyc mocha "test/unit/**/*.spec.ts"` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 185 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 185 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 184 | `mocha js` | 
| [ClickSimply/Nano-SQL](https://github.com/ClickSimply/Nano-SQL) | 184 | `mocha -r ts-node/register tests/index.ts` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 182 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 181 | `cross-env NODE_ENV=test mocha` | 
| [jacobbogers/blasjs](https://github.com/jacobbogers/blasjs) | 179 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [bmewburn/intelephense](https://github.com/bmewburn/intelephense) | 173 | `mocha -r ts-node/register test/*.ts` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 173 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 171 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 170 | `npm run lint && npm run mocha` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 169 | `nyc mocha --recursive test/**/*.ts` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 168 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 167 | `npm run clean && npm run build && npm run lint && mocha` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 166 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 164 | `mocha-webpack "src/**/*.ts"` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 164 | `npm run build && npm run mocha` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 161 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 161 | `mocha "test/**/*.spec.ts"` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 159 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 156 | `mocha lib/spec/core` | 
| [square/babel-codemod](https://github.com/square/babel-codemod) | 155 | `mocha "test/**/*Test.js"` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 155 | `tsc && cd dist && mocha` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 154 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 149 | `mocha --timeout 10000 -u tdd ./out/tests/` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 147 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [emmanueltouzery/prelude.ts](https://github.com/emmanueltouzery/prelude.ts) | 142 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 136 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [calidion/vig](https://github.com/calidion/vig) | 135 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [Azure/azure-functions-pack](https://github.com/Azure/azure-functions-pack) | 133 | `npm run build && mocha --compilers ts:ts-node/register --recursive test/**/*-spec.ts` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 132 | `tsc && mocha` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 131 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [hydux/hydux](https://github.com/hydux/hydux) | 131 | `npm run mocha -- "src/test/unit/*.test.ts"` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 131 | `mocha -r ts-node/register test/*.ts` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 131 | `TEST_BROWSER_DRIVER=phantomjs meteor test --driver-package=ardatan:mocha` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 129 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 129 | `mocha` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 128 | `mocha test/unit/ --exit` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 127 | `mocha --require ts-node/register test/**/*.ts` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 127 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [nspragg/filehound](https://github.com/nspragg/filehound) | 125 | `mocha -r ts-node/register test/*.ts` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [TrustWallet/trust-ray](https://github.com/TrustWallet/trust-ray) | 124 | `cross-env NODE_ENV=test mocha --recursive --require ts-node/register 'test/**/*.test.ts' --exit` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 124 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [DotJoshJohnson/vscode-xml](https://github.com/DotJoshJohnson/vscode-xml) | 123 | `npm run compile && mocha ./out/test/**/*.js` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 122 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 121 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 121 | `istanbul test -- _mocha` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 121 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 119 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 119 | `mocha --require source-map-support/register dist/test` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 118 | `gulp compile && mocha` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 118 | `mocha test` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 118 | `mocha lib/test` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 118 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 118 | `mocha --timeout 10000` | 
| [prh/prh](https://github.com/prh/prh) | 116 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [VirgilSecurity/demo-twilio-chat-js](https://github.com/VirgilSecurity/demo-twilio-chat-js) | 114 | `mocha --timeout 5000 -r ts-node/register -r tsconfig-paths/register ./api/tests/*.test.ts` | 
| [cartant/rxjs-marbles](https://github.com/cartant/rxjs-marbles) | 114 | `yarn run lint && yarn run test:build && cross-env FAILING=0 yarn run test:ava && cross-env FAILING=0 yarn run test:jasmine && cross-env FAILING=0 yarn run test:jasmine-angular && cross-env FAILING=0 yarn run test:jest && cross-env FAILING=0 yarn run test:mocha && cross-env FAILING=0 yarn run test:tape` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 114 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 114 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 112 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 112 | `npm run-script build && mocha --opts test/mocha.opts build/test` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 109 | `mocha` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 108 | `cross-env NODE_ENV=test mocha --exit` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 107 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [gamestdio/colyseus.js](https://github.com/gamestdio/colyseus.js) | 107 | `mocha test/*.ts --require ts-node/register` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 106 | `mocha -R spec dist/test/**/*.js` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 104 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 103 | `mocha --full-trace tests/test.js` | 
| [Soluto/graphql-to-mongodb](https://github.com/Soluto/graphql-to-mongodb) | 103 | `ts-mocha tests/**/*.spec.ts` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 101 | `tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 101 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 101 | `cd test && mocha -r ts-node/register *.ts` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 100 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 100 | `webpack && mocha-phantomjs test/index.html` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 98 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 97 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 96 | `npm-run-all build test:mocha test:coverage lint` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 96 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 95 | `mocha ./spec/*.js` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 95 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 95 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 94 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 93 | `mocha --compilers ts:ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 93 | `tsc; mocha --recursive test/suite/` | 
| [filestack/filestack-js](https://github.com/filestack/filestack-js) | 93 | `npm run build && concurrently -r --kill-others 'npm run prism:mock' 'npm run toxy' 'npm run lint && TEST_ENV=unit karma start && TEST_ENV=unit nyc mocha'` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 93 | `mocha` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 92 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 92 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 92 | `node node_modules/mocha/bin/mocha` | 
| [MichaelSolati/geofirestore](https://github.com/MichaelSolati/geofirestore) | 92 | `nyc --reporter=html --reporter=text mocha` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 91 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 91 | `mocha --recursive -t 4000` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 90 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 90 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 89 | `mocha` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 89 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 89 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 89 | `mocha` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 89 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 89 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 89 | `mocha test/* --timeout 500000` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 88 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 88 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 88 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 88 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 87 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [wonderful-panda/vue-tsx-support](https://github.com/wonderful-panda/vue-tsx-support) | 85 | `npm-run-all prettier tsc-test mocha` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 85 | `mocha ./dist/test --recursive` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 85 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register 'test/**/*.ts'` | 
| [nicksenger/react-arcgis](https://github.com/nicksenger/react-arcgis) | 85 | `nyc mocha` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 85 | `mocha test/ --recursive` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 84 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 83 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 83 | `nyc mocha --require espower-typescript/guess --require source-map-support/register "test/**/*.test.ts"` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 82 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 82 | `mocha` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 82 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 80 | `nyc npm run _mocha` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 79 | `npm run lint && npm run prettier && npm run mocha` | 
| [dsherret/ts-nameof](https://github.com/dsherret/ts-nameof) | 79 | `npm run --silent copy-test-files && nyc --reporter=lcov mocha --opts mocha.opts` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 76 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 74 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 74 | `mocha --compilers js:babel-core/register --recursive` | 
| [AlexGalays/spacelift](https://github.com/AlexGalays/spacelift) | 74 | `mocha test/test.js && mocha --ui tdd test/option.js && mocha --ui tdd test/result.js` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 74 | `mocha --require ts-node/register test/**/*.ts` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 74 | `mocha` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 73 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 73 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 73 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 73 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 73 | `npm run lint && nyc mocha` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 72 | `nyc mocha --recursive test/**/*.ts` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 71 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 70 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 70 | `mocha --ui tdd out/test/extension.test.js` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 69 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 69 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [httptoolkit/mockttp](https://github.com/httptoolkit/mockttp) | 69 | `npm run build && npm run test:mocha && npm run test:browser` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 68 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 68 | `npm run lint && npm run mocha` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 68 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 68 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [AugurProject/augur-node](https://github.com/AugurProject/augur-node) | 65 | `mocha test/unit` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 65 | `mocha -r ts-node/register 'test/main.js'` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 65 | `mocha -r ts-node/register test/*.ts` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 65 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 65 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 64 | `mocha -u tdd ./out/tests/` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 64 | `mocha build/test` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 64 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 63 | `npm run compile && mocha && npm run lint` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 63 | `mocha out/**/*.spec.js` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 62 | `tsc && mocha "dist/test/**/*.js" ` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 61 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [wix/rawss](https://github.com/wix/rawss) | 61 | `mocha` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 61 | `nyc mocha lib/**/*Test.js` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 61 | `mocha 'lib/**/__tests__/*.js'` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 61 | `mocha dist/test/*.js` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 60 | `TS_NODE_FILES=true mocha --timeout 20000 --slow 6000 --require ts-node/register "src/test/test*.ts"` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 60 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 59 | `nyc mocha` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 59 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 58 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 58 | `mocha -r ./src/test/common/setup.ts ./lib/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 58 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 58 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 58 | `nyc mocha` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 57 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 57 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 56 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [puzzle-js/PuzzleJs](https://github.com/puzzle-js/PuzzleJs) | 55 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 55 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 55 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 54 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 54 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 53 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 53 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 53 | `npm run build && npm run mocha` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 53 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 53 | `nyc mocha --opts .mocha.opts` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 53 | `mocha` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 53 | `nyc mocha build/test` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 52 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 52 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 52 | `mocha build/tests/index.js` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 52 | `mocha --timeout 30000 test/**/*.js` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 52 | `mocha --recursive` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 52 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 51 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 51 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 51 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 51 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 51 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 51 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 51 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 51 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 50 | `NODE_ENV=test nyc mocha` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 50 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 50 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [indutny/llparse](https://github.com/indutny/llparse) | 49 | `npm run mocha && npm run lint` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 49 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [DhyanaChina/todo-live](https://github.com/DhyanaChina/todo-live) | 49 | `mocha` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 48 | `NODE_ENV=test nyc mocha` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 48 | `mocha --timeout 10000 --slow 2500 tests/all-test-cases.js` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 48 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 48 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd ./out/test/extension.test.js` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 48 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 47 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 47 | `mocha --compilers ts:ts-node/register --recursive` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 47 | `node_modules/.bin/istanbul cover node_modules/.bin/_mocha -- --bail --check-leaks dist/test` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 47 | `mocha` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 46 | `tsc --version && tsc && mocha out/test` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 46 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 45 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [DhyanaChina/koa2-typescript-guide](https://github.com/DhyanaChina/koa2-typescript-guide) | 45 | `mocha` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 45 | `npm run compile && mocha && npm run lint` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 45 | `mocha .tmp/spec/index.spec.js` | 
| [SPGoding/spu](https://github.com/SPGoding/spu) | 45 | `mocha --require espower-typescript/guess "./src/tests/**/*.ts"` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 44 | `mocha --opts config/mocha.opts` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 44 | `mocha --ui qunit` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 44 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 44 | `mocha -R spec ./test` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 44 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 44 | `nyc mocha --opts test/mocha.opts` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 43 | `cross-env NODE_ENV=test mocha` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 43 | `mocha --opts spec/mocha.opts spec/**/*-spec.ts` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 43 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 43 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [balmbees/dynamo-typeorm](https://github.com/balmbees/dynamo-typeorm) | 43 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 42 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 42 | `mocha out/{,**/}*.spec.js -s 0` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 42 | `mocha test` | 
| [zswang/icity](https://github.com/zswang/icity) | 42 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 41 | `mocha` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 41 | `npm run lint && mocha dist/spec` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 41 | `npm run compile && mocha` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 41 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [indutny/llhttp](https://github.com/indutny/llhttp) | 41 | `npm run mocha && npm run lint` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 41 | `nyc mocha` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 41 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 41 | `tsc && mocha build/test` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 40 | `mocha --opts mocha.opts --watch` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 40 | `node_modules/.bin/mocha` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 40 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 40 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 40 | `mocha && npm run aplus` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 40 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 40 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 40 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 40 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 39 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 39 | `mocha --opts cli-test-mocha.opts` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 39 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 39 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 39 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 39 | `node_modules/.bin/mocha --watch` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 39 | `mocha --opts test/mocha.opts` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 39 | `mocha out/test` | 
| [willryan/factory.ts](https://github.com/willryan/factory.ts) | 39 | `NODE_ENV=test mocha --require spec/setup.js --require ts-node/register` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 39 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 39 | `mocha index.test.js` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 39 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [webix-hub/webix-jet](https://github.com/webix-hub/webix-jet) | 39 | `webpack && phantomjs node_modules/mocha-phantomjs-core/mocha-phantomjs-core.js tests/index.html spec` | 
| [aurelia/bundler](https://github.com/aurelia/bundler) | 39 | `mocha --reporter spec --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 39 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 38 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 38 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 38 | `mocha --require ts-node/register tests/**/*.ts` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 38 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 38 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 38 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 37 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 37 | `tsc && mocha dist/**/*.spec.js` | 
| [utopian-io/api.utopian.io](https://github.com/utopian-io/api.utopian.io) | 37 | `cross-env NODE_ENV=test npx mocha --ui bdd --reporter spec --colors --recursive -r ts-node/register tests/index.ts` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 37 | `nyc mocha --require source-map-support/register --require ts-node/register test/**/*.ts` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 37 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 37 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 36 | `tsc && npm run lint && mocha` | 
| [Polymer/polymer-linter](https://github.com/Polymer/polymer-linter) | 36 | `npm run build && mocha && npm run lint` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 36 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 36 | `mocha` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 36 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 35 | `mocha test/*.js` | 
| [fyndme/messenger-bot-tester](https://github.com/fyndme/messenger-bot-tester) | 35 | `mocha ./test-build` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 35 | `npm run prettier && npm run lint && npm run mocha` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 35 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 35 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 35 | `mocha test/*.js` | 
| [fyndme/messenger-bot-tester](https://github.com/fyndme/messenger-bot-tester) | 35 | `mocha ./test-build` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 35 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 35 | `npm run prettier && npm run lint && npm run mocha` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 35 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 35 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 35 | `mocha --reporter spec` | 
| [tgreyjs/typedoc-plugin-markdown](https://github.com/tgreyjs/typedoc-plugin-markdown) | 35 | `mocha test/test.js` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 34 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [Draccoz/twc](https://github.com/Draccoz/twc) | 34 | `npm run lint && mocha --require ts-node/register --ui bdd tests/tests.spec.ts` | 
| [davetemplin/web-request](https://github.com/davetemplin/web-request) | 34 | `mocha` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 34 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [forthright/vile](https://github.com/forthright/vile) | 34 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [paralin/grpc-bus](https://github.com/paralin/grpc-bus) | 34 | `npm run lint && npm run mocha` | 
| [qtumproject/qtumjs](https://github.com/qtumproject/qtumjs) | 34 | `mocha  lib/*_test.js` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 34 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [infinum/mobx-collection-store](https://github.com/infinum/mobx-collection-store) | 34 | `NODE_ENV=test nyc mocha` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 33 | `mocha --opts ./mocha.opts` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 33 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 33 | `mocha` | 
| [evebook/api](https://github.com/evebook/api) | 33 | `nyc --require ts-node/register mocha src/**/*.spec.ts --reporter spec` | 
| [agea/CmisJS](https://github.com/agea/CmisJS) | 33 | `tsc && mocha dist/**/*.spec.js` | 
| [userpixel/typescript](https://github.com/userpixel/typescript) | 33 | `mocha test` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 33 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 33 | `npm run mocha && npm run lint` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 33 | `tsc && mocha spec/` | 
| [mixi-inc/css-semdiff](https://github.com/mixi-inc/css-semdiff) | 32 | `mocha --opts mocha.opts './dist/**/*.test.js'` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 32 | `mocha --recursive` | 
| [igorzg/typeix](https://github.com/igorzg/typeix) | 32 | `npm run compile && mocha build/tests/ --debug --full-trace` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 32 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 32 | `cross-env NODE_ENV=test nyc mocha test/**/*.ts` | 
| [GoodgameStudios/RobotlegsJS](https://github.com/GoodgameStudios/RobotlegsJS) | 32 | `nyc mocha` | 
| [supergraphql/supergraph](https://github.com/supergraphql/supergraph) | 32 | `nyc mocha ./dist/**/*.spec.js` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 31 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 31 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [NikitchenkoSergey/scheme-designer](https://github.com/NikitchenkoSergey/scheme-designer) | 31 | `mocha` | 
| [ForbesLindesay/barrage](https://github.com/ForbesLindesay/barrage) | 31 | `mocha -R spec lib/test.js` | 
| [davetemplin/async-parallel](https://github.com/davetemplin/async-parallel) | 31 | `mocha` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 31 | `mocha` | 
| [haoliangyu/boundary.now](https://github.com/haoliangyu/boundary.now) | 31 | `mocha test/**/*.test.ts --require ts-node/register --require reflect-metadata` | 
| [mulesoft-labs/yaml-ast-parser](https://github.com/mulesoft-labs/yaml-ast-parser) | 31 | `npm run build && mocha --ui tdd dist/test` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 31 | `mocha --recursive "dist/**/*.test.js"` | 
| [Rich-Harris/port-authority](https://github.com/Rich-Harris/port-authority) | 31 | `mocha --opts mocha.opts` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 31 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [secret-tech/backend-token-wallets](https://github.com/secret-tech/backend-token-wallets) | 31 | `mocha -r ts-node/register -r test/prepare.ts src/**/*.spec.ts` | 
| [mrmlnc/vscode-stylefmt](https://github.com/mrmlnc/vscode-stylefmt) | 30 | `mocha out/**/*.spec.js -s 0` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 30 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [tsframework/ts-framework](https://github.com/tsframework/ts-framework) | 30 | `mocha build-test --recursive` | 
| [leizongmin/leizm-web](https://github.com/leizongmin/leizm-web) | 30 | `npm run format && mocha --require ts-node/register --exit "src/test/**/*.ts"` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 30 | `tsc -p .tsconfig.test.json && mocha` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 30 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [siegebell/vsc-prettify-symbols-mode](https://github.com/siegebell/vsc-prettify-symbols-mode) | 30 | `tsc -p ./ && mocha -u tdd ./out/test` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 30 | `nyc mocha` | 
| [Azure/oav](https://github.com/Azure/oav) | 29 | `npm run tsc && npm run tslint && nyc mocha ./test/**/*.ts -r ts-node/register -t 10000` | 
| [gwuhaolin/spring-data-rest-js](https://github.com/gwuhaolin/spring-data-rest-js) | 29 | `tsc & mocha` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 29 | `mocha` | 
| [Jiasm/typescript-example](https://github.com/Jiasm/typescript-example) | 29 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [creeperyang/id3-parser](https://github.com/creeperyang/id3-parser) | 29 | `TS_NODE_PROJECT='test/tsconfig.json' mocha --require ts-node/register 'test/*.spec.ts' --reporter dot` | 
| [codefoster/waterrower](https://github.com/codefoster/waterrower) | 29 | `mocha test` | 
| [rhysd/electron-in-page-search](https://github.com/rhysd/electron-in-page-search) | 29 | `electron-mocha --timeout 10000 --renderer test/*.js` | 
| [nicolastakashi/linq-to-type](https://github.com/nicolastakashi/linq-to-type) | 29 | `nyc mocha` | 
| [nilobarp/text2json](https://github.com/nilobarp/text2json) | 29 | `DEBUG=TP* mocha dist/test/spectrum-tests.js` | 
| [googleapis/google-cloud-kvstore](https://github.com/googleapis/google-cloud-kvstore) | 29 | `nyc mocha build/test` | 
| [ShieldBattery/node-interval-tree](https://github.com/ShieldBattery/node-interval-tree) | 29 | `mocha -R spec --compilers ts:ts-node/register test/*.ts` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 29 | `mocha test/unit` | 
| [palmerabollo/bingspeech-api-client](https://github.com/palmerabollo/bingspeech-api-client) | 29 | `npm run build && mocha -R spec 'lib/**/*.spec.js'` | 
| [3VLINC/graphql-to-typescript](https://github.com/3VLINC/graphql-to-typescript) | 29 | `mocha "dist/**/*.test.js"` | 
| [coderfox/clover](https://github.com/coderfox/clover) | 29 | `nyc mocha` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 29 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [patrimart/monadness-js](https://github.com/patrimart/monadness-js) | 29 | `./node_modules/.bin/istanbul cover ./node_modules/mocha/bin/_mocha --report lcovonly -- -R spec && cat ./coverage/lcov.info | ./node_modules/coveralls/bin/coveralls.js && rm -rf ./coverage` | 
| [mseemann/js-restful-express](https://github.com/mseemann/js-restful-express) | 28 | `istanbul cover node_modules/mocha/bin/_mocha --report lcov -x '*.spec.*'  -- -c --check-leaks --require ts-node/register --require core-js --recursive --reporter spec src/**/*.spec.ts` | 
| [bespoken/virtual-device-sdk](https://github.com/bespoken/virtual-device-sdk) | 28 | `nyc mocha lib/test/*Test.js` | 
| [ERCdEX/automation-toolkit](https://github.com/ERCdEX/automation-toolkit) | 28 | `rm -rf ./test-data && NODE_ENV=test mocha -t 15000 -r ts-node/register src/**/*.spec.ts` | 
| [NE-LOAN-FED/NE-Component](https://github.com/NE-LOAN-FED/NE-Component) | 28 | `mocha --compilers js:babel-register --recursive` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 28 | `atool-test-mocha ./src/**/*-test.js` | 
| [alitaheri/jss-rtl](https://github.com/alitaheri/jss-rtl) | 28 | `mocha --require ts-node/register "src/**/*.spec.ts"` | 
| [georgehanson/Vue-Form-Components](https://github.com/georgehanson/Vue-Form-Components) | 28 | `mocha-webpack --webpack-config="webpack.test.config.js" --require="tests/setup.ts" tests/**/*.spec.ts` | 
| [tbluemel/rtf.js](https://github.com/tbluemel/rtf.js) | 28 | `mocha test/test.js` | 
| [VaclavObornik/di-ts](https://github.com/VaclavObornik/di-ts) | 28 | `node ./node_modules/mocha/bin/mocha ./spec/ --recursive --require reflect-metadata` | 
| [AsynkronIT/protoactor-js](https://github.com/AsynkronIT/protoactor-js) | 27 | `mocha --opts test/mocha.opts -w` | 
| [cartant/firebase-nightlight](https://github.com/cartant/firebase-nightlight) | 27 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [fsahmad/typescript-uml](https://github.com/fsahmad/typescript-uml) | 27 | `npm run build && mocha --compilers ts:ts-node/register --recursive 'src/**/*-spec.ts'` | 
| [lazerwalker/storyboard](https://github.com/lazerwalker/storyboard) | 27 | `mocha-webpack tests` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 27 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [masvis/angular4-hal](https://github.com/masvis/angular4-hal) | 27 | `mocha -r ts-node/register --config=test/test-config.json test/*.test.ts` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 27 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [ClickerMonkey/vuex-router-actions](https://github.com/ClickerMonkey/vuex-router-actions) | 27 | `mocha -r ts-node/register tests/**/*.ts` | 
| [vrudikov/typescript-rest-boilerplate](https://github.com/vrudikov/typescript-rest-boilerplate) | 27 | `cross-env NODE_ENV=test mocha` | 
| [TomShacham/http4js](https://github.com/TomShacham/http4js) | 27 | `tsc; mocha --require ts-node/register 'src/{test,ssl}/**/*.ts'` | 
| [alexeagle/tsetse](https://github.com/alexeagle/tsetse) | 26 | `tsc && mocha built/test/*.js` | 
| [sebsylvester/botbuilder-wit](https://github.com/sebsylvester/botbuilder-wit) | 26 | `nyc --reporter=lcov mocha` | 
| [glixlur/jsx-dom](https://github.com/glixlur/jsx-dom) | 26 | `nyc --reporter=html mocha ./test/test.tsx --require ts-node/register` | 
| [tipether/tipether](https://github.com/tipether/tipether) | 26 | `mocha --require ts-node/register test/**/*.ts` | 
| [acrazing/mobx-sync](https://github.com/acrazing/mobx-sync) | 26 | `mocha --require ts-node/register --slow 1000 ./src/**/*.spec.ts` | 
| [alexanderwe/checksum-validator](https://github.com/alexanderwe/checksum-validator) | 26 | `mocha` | 
| [windwp/vscode-expand-region](https://github.com/windwp/vscode-expand-region) | 26 | `mocha --ui tdd --recursive "out/**/*.test.js"` | 
| [larshp/abaplint](https://github.com/larshp/abaplint) | 26 | `mocha --recursive --reporter progress build/test` | 
| [tusharmath/observable-air](https://github.com/tusharmath/observable-air) | 26 | `tsc && mocha --reporter=min` | 
| [RxParse/Parse-SDK-ts](https://github.com/RxParse/Parse-SDK-ts) | 26 | `node .bin/test/utils/init.js && mocha --timeout 30000 $(find .bin/test -name '*.js')` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 26 | `mocha` | 
| [nemtech/nem2-sdk-typescript-javascript](https://github.com/nemtech/nem2-sdk-typescript-javascript) | 26 | `mocha --ui bdd --recursive ./dist/test --timeout 90000` | 