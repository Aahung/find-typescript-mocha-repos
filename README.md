# Find Repos in TypeScript Tested using Mocha

The list was updated at 01:55:21 11/10/18 PST

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 63618 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 15683 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 9912 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 9080 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [sveltejs/svelte](https://github.com/sveltejs/svelte) | 8306 | `mocha --opts mocha.opts` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 6911 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 6006 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 5066 | `npm run mocha` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4496 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4179 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3345 | `mocha --opts mocha.opts` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 2917 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2786 | `mocha` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2565 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2417 | `mocha 'test/**/*.ts'` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 2373 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2116 | `mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1833 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1808 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1793 | `mocha` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1699 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [burtonator/polar-bookshelf](https://github.com/burtonator/polar-bookshelf) | 1526 | `find web/js -name '*Test.js' | xargs mocha-parallel-tests --timeout 10000 --max-parallel=1 --exit` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1365 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1322 | `nyc -x '' mocha` | 
| [gamestdio/colyseus](https://github.com/gamestdio/colyseus) | 1272 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1232 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [funkia/list](https://github.com/funkia/list) | 1197 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1158 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1154 | `mocha --opts mocha.opts` | 
| [shanalikhan/code-settings-sync](https://github.com/shanalikhan/code-settings-sync) | 1106 | `npm run vscode:prepublish && node ./node_modules/bin/mocha --recursive` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 1103 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1081 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1079 | `nyc --reporter=html --reporter=text mocha` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 1014 | `tsc -p ./ && mocha` | 
| [google/clasp](https://github.com/google/clasp) | 984 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [itchio/itch](https://github.com/itchio/itch) | 939 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 921 | `mocha --opts test/mocha.opts` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 879 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 819 | `mocha bin/tests/test.js` | 
| [netgusto/nodebook](https://github.com/netgusto/nodebook) | 752 | `mocha test/backend` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 726 | `yarn run lint && yarn run test:mocha` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 709 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 688 | `mocha --compilers ts:ts-node/register test/*.js || true` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 684 | `mocha` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 680 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 649 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 647 | `mocha --recursive` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 639 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 638 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 603 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 587 | `npm run lint && npm run mocha` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 587 | `mocha "out/**/*.spec.js" -s 0` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 569 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 549 | `mocha` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 545 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 541 | `mocha test` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 535 | `mocha --opts test/mocha.opts dist/test` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 526 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 519 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 519 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 502 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 499 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 477 | `mocha --opts mocha.opts` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 462 | `npm run build && mocha` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 455 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 445 | `mocha --opts mocha.opts` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 442 | `_mocha --` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 437 | `npm run mocha` | 
| [dsherret/ts-simple-ast](https://github.com/dsherret/ts-simple-ast) | 432 | `cross-env TS_NODE_COMPILER="ttypescript" TS_NODE_TRANSPILE_ONLY="true" mocha --opts mocha.opts` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 429 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 424 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 424 | `cross-env NODE_ENV=test mocha **/*.spec.ts --compilers ts:ts-node/register` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 412 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [Romakita/ts-express-decorators](https://github.com/Romakita/ts-express-decorators) | 412 | `npm run clean && npm run tsc && npm run tslint && cross-env NODE_ENV=test nyc --reporter=html --reporter=text _mocha --recursive` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 406 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 391 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 384 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 384 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 380 | `cd test && mocha -r ts-node/register *.ts` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 378 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [R-js/libRmath.js](https://github.com/R-js/libRmath.js) | 370 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 359 | `mocha` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 348 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 345 | `npm run build && mocha` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 329 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 329 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 307 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 304 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [Microsoft/node-pty](https://github.com/Microsoft/node-pty) | 294 | `cross-env NODE_ENV=test mocha -R spec --exit lib/*.test.js` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 292 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 290 | `mocha` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 280 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 273 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 273 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 272 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 270 | `mocha --compilers js:babel-register test/**/*.js` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 268 | `mocha` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 267 | `mocha test` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 267 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 266 | `mocha lib/test` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 264 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 258 | `mocha src/**/*.spec.ts` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 249 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts view/test/test-heightmap.ts` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 249 | `mocha` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 248 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 241 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 238 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 235 | `mocha "test/**/*.spec.ts"` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 232 | `tsc && mocha` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 227 | `tsc && mocha dist/**/*.spec.js` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 226 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 225 | `nyc --reporter html mocha` | 
| [dubzzz/fast-check](https://github.com/dubzzz/fast-check) | 224 | `npm run build && nyc mocha "test/unit/**/*.spec.ts"` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 216 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 209 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 206 | `mocha test` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 203 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 200 | `mocha -R spec test/integration` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 200 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 199 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [ClickSimply/Nano-SQL](https://github.com/ClickSimply/Nano-SQL) | 198 | `mocha -r ts-node/register tests/index.ts` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 197 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 197 | `mocha dist/test.js` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 196 | `mocha-webpack "src/**/*.ts"` | 
| [Zarel/Pokemon-Showdown-Client](https://github.com/Zarel/Pokemon-Showdown-Client) | 195 | `eslint --config=.eslintrc.js --cache --cache-file=eslint-cache/base js/ && eslint --config=build-tools/.eslintrc.js --cache --cache-file=eslint-cache/build build-tools/update build-tools/build-indexes && tsc && node build && mocha` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 193 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [R-js/blasjs](https://github.com/R-js/blasjs) | 191 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 191 | `cross-env NODE_ENV=test mocha` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 186 | `mocha js` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 184 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [AmirTugi/tea-school](https://github.com/AmirTugi/tea-school) | 183 | `npx ts-mocha ./src/tests/**.ts` | 
| [bmewburn/intelephense](https://github.com/bmewburn/intelephense) | 180 | `mocha -r ts-node/register test/*.ts` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 180 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 175 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 175 | `nyc mocha --recursive test/**/*.ts` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 172 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 172 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 170 | `npm run lint && npm run mocha` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 169 | `npm run build && npm run mocha` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 168 | `mocha lib/spec/core` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 167 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 167 | `npm run clean && npm run build && npm run lint && mocha` | 
| [square/babel-codemod](https://github.com/square/babel-codemod) | 163 | `mocha "test/**/*Test.js"` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 162 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 158 | `tsc && cd dist && mocha` | 
| [Chinachu/Mirakurun](https://github.com/Chinachu/Mirakurun) | 154 | `mocha --exit test/*.spec.js` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 153 | `gulp compile && mocha --timeout 10000 -u tdd ./out/tests/` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 153 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [emmanueltouzery/prelude.ts](https://github.com/emmanueltouzery/prelude.ts) | 150 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 147 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [calidion/vig](https://github.com/calidion/vig) | 145 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 145 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | 141 | `nyc mocha` | 
| [hydux/hydux](https://github.com/hydux/hydux) | 139 | `npm run mocha -- "src/test/unit/*.test.ts"` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 139 | `mocha test/unit` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 137 | `tsc && mocha` | 
| [Azure/azure-functions-pack](https://github.com/Azure/azure-functions-pack) | 135 | `npm run build && mocha --compilers ts:ts-node/register --recursive test/**/*-spec.ts` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 134 | `cd test && mocha -r ts-node/register *.ts` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 133 | `mocha` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 132 | `mocha -r ts-node/register test/*.ts` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 131 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 131 | `mocha test/unit/ --exit` | 
| [nspragg/filehound](https://github.com/nspragg/filehound) | 131 | `mocha -r ts-node/register test/*.ts` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 131 | `mocha lib/test` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 130 | `TEST_BROWSER_DRIVER=phantomjs meteor test --driver-package=ardatan:mocha` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 129 | `mocha --require ts-node/register test/**/*.ts` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 129 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 129 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 127 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [DotJoshJohnson/vscode-xml](https://github.com/DotJoshJohnson/vscode-xml) | 126 | `npm run compile && mocha ./out/test/**/*.js` | 
| [TrustWallet/trust-ray](https://github.com/TrustWallet/trust-ray) | 126 | `cross-env NODE_ENV=test mocha --recursive --require ts-node/register 'test/**/*.test.ts' --exit` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 125 | `gulp compile && mocha` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 125 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [cartant/rxjs-marbles](https://github.com/cartant/rxjs-marbles) | 124 | `yarn run lint && yarn run test:build && cross-env FAILING=0 yarn run test:ava && cross-env FAILING=0 yarn run test:jasmine && cross-env FAILING=0 yarn run test:jasmine-angular && cross-env FAILING=0 yarn run test:jest && cross-env FAILING=0 yarn run test:mocha && cross-env FAILING=0 yarn run test:tape` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 123 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 122 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 121 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 121 | `istanbul test -- _mocha` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 121 | `mocha --require source-map-support/register dist/test` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 120 | `mocha --timeout 10000` | 
| [prh/prh](https://github.com/prh/prh) | 119 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 119 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 118 | `mocha test` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 118 | `npm run-script build && mocha --opts test/mocha.opts build/test/config.js build/test` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 118 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 117 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 114 | `cross-env NODE_ENV=test mocha --exit` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 114 | `mocha` | 
| [Soluto/graphql-to-mongodb](https://github.com/Soluto/graphql-to-mongodb) | 113 | `ts-mocha tests/**/*.spec.ts` | 
| [VirgilSecurity/demo-twilio-chat-js](https://github.com/VirgilSecurity/demo-twilio-chat-js) | 112 | `mocha --timeout 5000 -r ts-node/register -r tsconfig-paths/register ./api/tests/*.test.ts` | 
| [gamestdio/colyseus.js](https://github.com/gamestdio/colyseus.js) | 112 | `mocha test/*.ts --require ts-node/register` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 110 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 110 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 110 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 110 | `nyc --reporter=html --reporter=text mocha` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 108 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 108 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 106 | `mocha -R spec dist/test/**/*.js` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 105 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 105 | `mocha --full-trace tests/test.js` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 104 | `webpack && mocha-phantomjs test/index.html` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 101 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 101 | `mocha --recursive -t 4000` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 100 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 100 | `mocha` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 99 | `npm-run-all build test:mocha test:coverage lint` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 99 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 99 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 99 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 98 | `tsc; mocha --recursive lib/ test/runner` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 98 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 98 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 97 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 96 | `mocha --compilers ts:ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 95 | `mocha ./spec/*.js` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 95 | `mocha ./spec/*.js` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 95 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [wildbit/postmark.js](https://github.com/wildbit/postmark.js) | 95 | `node_modules/mocha/bin/mocha --timeout 10000 --retries 1 -r ts-node/register test/**/*test.ts` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 95 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 94 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 94 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 93 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 93 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 93 | `mocha` | 
| [nicksenger/react-arcgis](https://github.com/nicksenger/react-arcgis) | 93 | `nyc mocha` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 93 | `node node_modules/mocha/bin/mocha` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 92 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 92 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 91 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 91 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [nucleojs/nucleo](https://github.com/nucleojs/nucleo) | 90 | `mocha -r ts-node/register` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 89 | `mocha --require espower-typescript/guess --require source-map-support/register "test/**/*.test.ts"` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 89 | `mocha test/* --timeout 500000` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 88 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 88 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 88 | `mocha test/ --recursive` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 87 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register 'test/**/*.ts'` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 87 | `npm run lint && npm run prettier && npm run mocha` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 87 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [dsherret/ts-nameof](https://github.com/dsherret/ts-nameof) | 87 | `yarn run --silent copy-test-files && nyc --reporter=lcov mocha --opts mocha.opts` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 86 | `mocha ./dist/test --recursive` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 86 | `mocha` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 85 | `nyc npm run _mocha` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 85 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 83 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 80 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 80 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 79 | `mocha` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 78 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [AlexGalays/spacelift](https://github.com/AlexGalays/spacelift) | 78 | `mocha test/test.js && mocha --ui tdd test/option.js && mocha --ui tdd test/result.js` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 77 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 77 | `mocha --require ts-node/register test/**/*.ts` | 
| [teambition/ReactiveDB](https://github.com/teambition/ReactiveDB) | 76 | `npm run lint && NODE_ENV=test tman --mocha spec-js/test/run.js` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 75 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 74 | `mocha --compilers js:babel-core/register --recursive` | 
| [CityOfZion/neo-js](https://github.com/CityOfZion/neo-js) | 74 | `./node_modules/.bin/mocha -b ./test/unit/**/*` | 
| [indutny/llparse](https://github.com/indutny/llparse) | 74 | `npm run mocha && npm run lint` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 74 | `mocha --ui tdd out/test/extension.test.js` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 73 | `nyc mocha --recursive test/**/*.ts` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 73 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 73 | `npm run lint && nyc mocha` | 
| [httptoolkit/mockttp](https://github.com/httptoolkit/mockttp) | 73 | `npm run build && npm run test:mocha && npm run test:browser` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 72 | `npm run lint && npm run mocha` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 72 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 70 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 70 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 70 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 69 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 69 | `mocha -r ts-node/register 'test/main.js'` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 67 | `tsc && mocha "dist/test/**/*.js" ` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 67 | `mocha build/test` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 67 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 66 | `mocha -u tdd ./out/tests/` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 66 | `nyc mocha` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 66 | `mocha -r ./src/test/common/setup.ts ./lib/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 66 | `mocha -r ts-node/register test/*.ts` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 66 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 65 | `npm run compile && mocha && npm run lint` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 65 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 64 | `nyc mocha lib/**/*Test.js` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 64 | `mocha out/**/*.spec.js` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 62 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 62 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 62 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 62 | `TS_NODE_FILES=true mocha --opts src/test/mocha.opts "src/test/test*.ts"` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 62 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 62 | `mocha 'lib/**/__tests__/*.js'` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 62 | `mocha dist/test/*.js` | 
| [puzzle-js/PuzzleJs](https://github.com/puzzle-js/PuzzleJs) | 61 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 61 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 60 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 60 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [wix/rawss](https://github.com/wix/rawss) | 60 | `mocha` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 60 | `nyc mocha` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 59 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 59 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 58 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 58 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 58 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 57 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 57 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 57 | `mocha build/tests/index.js` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 56 | `nyc mocha build/test` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 55 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 55 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 54 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 54 | `npm run build && npm run mocha` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 54 | `mocha --timeout 30000 test/**/*.js` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 54 | `mocha --recursive` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 54 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd ./out/test/extension.test.js` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 53 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 53 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 53 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 53 | `nyc mocha --opts .mocha.opts` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 53 | `mocha` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 53 | `mocha` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 53 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 52 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 52 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 52 | `mocha --timeout 10000 --slow 2500 tests/unittests/**/*.spec.js tests/functional-test-cases.js` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 52 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 52 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 52 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [indutny/llhttp](https://github.com/indutny/llhttp) | 51 | `npm run mocha && npm run lint` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 51 | `mocha --opts spec/mocha.opts spec/**/*-spec.ts` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [DhyanaChina/todo-live](https://github.com/DhyanaChina/todo-live) | 51 | `mocha` | 
| [DhyanaChina/koa2-typescript-guide](https://github.com/DhyanaChina/koa2-typescript-guide) | 50 | `mocha` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 50 | `NODE_ENV=test nyc mocha` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 50 | `NODE_ENV=test nyc mocha` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 50 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 49 | `mocha` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 49 | `mocha .tmp/spec/index.spec.js` | 
| [mono/TsToCSharp](https://github.com/mono/TsToCSharp) | 49 | `npm run lint && mocha  ./dist/TsToCSharpTests.js` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 48 | `mocha --ui qunit` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 48 | `tsc --version && tsc && mocha out/test` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 48 | `node_modules/.bin/nyc npm run mocha` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 48 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 47 | `cross-env NODE_ENV=test mocha` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 47 | `mocha` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 47 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 47 | `mocha --compilers ts:ts-node/register --recursive` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 47 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 46 | `mocha --opts config/mocha.opts` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 46 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 45 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 45 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 45 | `nyc mocha` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 45 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 45 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [CommandBlockLogic/spu](https://github.com/CommandBlockLogic/spu) | 45 | `mocha --require espower-typescript/guess "./src/test/**/*.ts"` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 45 | `nyc mocha --opts test/mocha.opts` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 45 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [balmbees/dynamo-types](https://github.com/balmbees/dynamo-types) | 45 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 44 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 44 | `npm run lint && mocha dist/spec` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 44 | `npm run compile && mocha` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 44 | `npm run compile && mocha && npm run lint` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 44 | `mocha --require ts-node/register tests/**/*.ts` | 
| [sourcegraph/browser-extensions](https://github.com/sourcegraph/browser-extensions) | 44 | `mocha --require ts-node/register --watch --watch-extensions ts './src/**/*.test.ts?(x)'` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 44 | `mocha` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 44 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 44 | `mocha -R spec ./test` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 44 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 44 | `nyc mocha` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 43 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 43 | `mocha --opts mocha.opts --watch` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 43 | `node_modules/.bin/mocha --watch` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 43 | `mocha --opts test/mocha.opts` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 43 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 43 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 43 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 42 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 42 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 42 | `mocha test` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 42 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 42 | `mocha index.test.js` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 42 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [roblox-ts/roblox-ts](https://github.com/roblox-ts/roblox-ts) | 42 | `nyc --reporter=html mocha --timeout 0 --require ts-node/register --require source-map-support/register --recursive src/test.ts` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 41 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 41 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 41 | `mocha test/*.js` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 41 | `mocha out/{,**/}*.spec.js -s 0` | 
| [Microsoft/typescript-tslint-plugin](https://github.com/Microsoft/typescript-tslint-plugin) | 41 | `mocha ./out/**/*.test.js --slow 2000 --timeout 10000` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 41 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [willryan/factory.ts](https://github.com/willryan/factory.ts) | 41 | `NODE_ENV=test mocha --require spec/setup.js --require ts-node/register` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 41 | `mocha out/test` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 41 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 41 | `tsc && mocha build/test` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 41 | `nyc mocha --require source-map-support/register --require ts-node/register test/**/*.ts` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 40 | `node_modules/.bin/mocha` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 40 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 40 | `mocha && npm run aplus` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 40 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 40 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 40 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 40 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 39 | `mocha --opts cli-test-mocha.opts` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 39 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 39 | `nyc mocha build/test` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 39 | `mocha` | 
| [webix-hub/webix-jet](https://github.com/webix-hub/webix-jet) | 39 | `webpack && phantomjs node_modules/mocha-phantomjs-core/mocha-phantomjs-core.js tests/index.html spec` | 
| [aurelia/bundler](https://github.com/aurelia/bundler) | 39 | `mocha --reporter spec --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 38 | `npm run prettier && npm run lint && npm run mocha` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 38 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 38 | `tsc && mocha dist/**/*.spec.js` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 38 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 38 | `npm run prettier && npm run lint && npm run mocha` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 38 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 38 | `tsc && mocha dist/**/*.spec.js` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 38 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 38 | `mocha --reporter spec` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 38 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 37 | `tsc && npm run lint && mocha` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 37 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [evebook/api](https://github.com/evebook/api) | 37 | `nyc --require ts-node/register mocha src/**/*.spec.ts --reporter spec` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 37 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [ethereum-ts/evm-ts](https://github.com/ethereum-ts/evm-ts) | 37 | `yarn lint && yarn test:mocha` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 37 | `mocha --recursive` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 37 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 37 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 37 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 36 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [Polymer/polymer-linter](https://github.com/Polymer/polymer-linter) | 36 | `npm run build && mocha && npm run lint` | 
| [utopian-io/api.utopian.io](https://github.com/utopian-io/api.utopian.io) | 36 | `cross-env NODE_ENV=test npx mocha --ui bdd --reporter spec --colors --recursive -r ts-node/register tests/index.ts` | 
| [ashleydavis/grademark](https://github.com/ashleydavis/grademark) | 36 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 36 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 35 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 35 | `mocha --opts ./mocha.opts` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 35 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [fyndme/messenger-bot-tester](https://github.com/fyndme/messenger-bot-tester) | 35 | `mocha ./test-build` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 35 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 35 | `mocha` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 35 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 35 | `cross-env NODE_ENV=test mocha test/**/*.ts` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 35 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [paralin/grpc-bus](https://github.com/paralin/grpc-bus) | 35 | `npm run lint && npm run mocha` | 
| [infinum/mobx-collection-store](https://github.com/infinum/mobx-collection-store) | 35 | `NODE_ENV=test nyc mocha` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 34 | `mocha` | 
| [agea/CmisJS](https://github.com/agea/CmisJS) | 34 | `tsc && mocha dist/**/*.spec.js` | 
| [Draccoz/twc](https://github.com/Draccoz/twc) | 34 | `npm run lint && mocha --require ts-node/register --ui bdd tests/tests.spec.ts` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 34 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [davetemplin/web-request](https://github.com/davetemplin/web-request) | 34 | `mocha` | 
| [forthright/vile](https://github.com/forthright/vile) | 34 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 34 | `tsc && mocha spec/` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 33 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [mixi-inc/css-semdiff](https://github.com/mixi-inc/css-semdiff) | 33 | `mocha --opts mocha.opts './dist/**/*.test.js'` | 
| [hg-pyun/iterize](https://github.com/hg-pyun/iterize) | 33 | `mocha --recursive ./test/*.ts --require ts-node/register` | 
| [userpixel/typescript](https://github.com/userpixel/typescript) | 33 | `mocha test` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 33 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [qtumproject/qtumjs](https://github.com/qtumproject/qtumjs) | 33 | `mocha  lib/*_test.js` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 33 | `npm run mocha && npm run lint` | 
| [supergraphql/supergraph](https://github.com/supergraphql/supergraph) | 33 | `nyc mocha ./dist/**/*.spec.js` | 
| [secret-tech/backend-token-wallets](https://github.com/secret-tech/backend-token-wallets) | 33 | `mocha -r ts-node/register -r test/prepare.ts src/**/*.spec.ts` | 
| [Jiasm/typescript-example](https://github.com/Jiasm/typescript-example) | 32 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [NikitchenkoSergey/scheme-designer](https://github.com/NikitchenkoSergey/scheme-designer) | 32 | `mocha` | 
| [davetemplin/async-parallel](https://github.com/davetemplin/async-parallel) | 32 | `mocha` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 32 | `mocha test/*.spec.ts` | 
| [igorzg/typeix](https://github.com/igorzg/typeix) | 32 | `npm run compile && mocha build/tests/ --debug --full-trace` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 32 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [GoodgameStudios/RobotlegsJS](https://github.com/GoodgameStudios/RobotlegsJS) | 32 | `nyc mocha` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 32 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [Rich-Harris/port-authority](https://github.com/Rich-Harris/port-authority) | 32 | `mocha --opts mocha.opts` | 
| [tsframework/ts-framework](https://github.com/tsframework/ts-framework) | 31 | `mocha build-test --recursive` | 
| [ForbesLindesay/barrage](https://github.com/ForbesLindesay/barrage) | 31 | `mocha -R spec lib/test.js` | 
| [leizongmin/leizm-web](https://github.com/leizongmin/leizm-web) | 31 | `npm run format && mocha --require ts-node/register --exit "src/test/**/*.ts"` | 
| [mulesoft-labs/yaml-ast-parser](https://github.com/mulesoft-labs/yaml-ast-parser) | 31 | `npm run build && mocha --ui tdd dist/test` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 31 | `tsc -p .tsconfig.test.json && mocha` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 31 | `atool-test-mocha ./src/**/*-test.js` | 
| [siegebell/vsc-prettify-symbols-mode](https://github.com/siegebell/vsc-prettify-symbols-mode) | 31 | `tsc -p ./ && mocha -u tdd ./out/test` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 31 | `mocha --recursive "dist/**/*.test.js"` | 
| [ste-vg/pop.svg](https://github.com/ste-vg/pop.svg) | 31 | `nyc mocha --require ./mocha.config.js -r ts-node/register 'src/**/*.spec.ts'  --exit --recursive --timeout 10000` | 
| [vrudikov/typescript-rest-boilerplate](https://github.com/vrudikov/typescript-rest-boilerplate) | 31 | `cross-env NODE_ENV=test mocha` | 
| [mrmlnc/vscode-stylefmt](https://github.com/mrmlnc/vscode-stylefmt) | 30 | `mocha out/**/*.spec.js -s 0` | 
| [acrazing/mobx-sync](https://github.com/acrazing/mobx-sync) | 30 | `mocha --require ts-node/register --slow 1000 ./src/**/*.spec.ts` | 
| [rhysd/electron-in-page-search](https://github.com/rhysd/electron-in-page-search) | 30 | `electron-mocha --timeout 10000 --renderer test/*.js` | 
| [fsahmad/typescript-uml](https://github.com/fsahmad/typescript-uml) | 30 | `npm run build && mocha --compilers ts:ts-node/register --recursive 'src/**/*-spec.ts'` | 
| [ShieldBattery/node-interval-tree](https://github.com/ShieldBattery/node-interval-tree) | 30 | `mocha -R spec --compilers ts:ts-node/register test/*.ts` | 
| [haoliangyu/boundary.now](https://github.com/haoliangyu/boundary.now) | 30 | `mocha test/**/*.test.ts --require ts-node/register --require reflect-metadata` | 
| [tbluemel/rtf.js](https://github.com/tbluemel/rtf.js) | 30 | `mocha test/test.js` | 
| [Azure/oav](https://github.com/Azure/oav) | 29 | `npm run tsc && npm run tslint && nyc mocha ./test/**/*.ts -r ts-node/register -t 10000 --reporter mocha-junit-reporter` | 
| [gwuhaolin/spring-data-rest-js](https://github.com/gwuhaolin/spring-data-rest-js) | 29 | `tsc & mocha` | 
| [codefoster/waterrower](https://github.com/codefoster/waterrower) | 29 | `mocha test` | 
| [creeperyang/id3-parser](https://github.com/creeperyang/id3-parser) | 29 | `TS_NODE_PROJECT='test/tsconfig.json' mocha --require ts-node/register 'test/*.spec.ts' --reporter dot` | 
| [nicolastakashi/linq-to-type](https://github.com/nicolastakashi/linq-to-type) | 29 | `nyc mocha` | 
| [nilobarp/text2json](https://github.com/nilobarp/text2json) | 29 | `DEBUG=TP* mocha dist/test/spectrum-tests.js` | 
| [googleapis/google-cloud-kvstore](https://github.com/googleapis/google-cloud-kvstore) | 29 | `nyc mocha build/test` | 
| [lazerwalker/storyboard](https://github.com/lazerwalker/storyboard) | 29 | `mocha-webpack tests` | 
| [bespoken/virtual-device-sdk](https://github.com/bespoken/virtual-device-sdk) | 29 | `nyc mocha lib/test/*Test.js` | 
| [palmerabollo/bingspeech-api-client](https://github.com/palmerabollo/bingspeech-api-client) | 29 | `npm run build && mocha -R spec 'lib/**/*.spec.js'` | 
| [alitaheri/jss-rtl](https://github.com/alitaheri/jss-rtl) | 29 | `mocha --require ts-node/register "src/**/*.spec.ts"` | 
| [3VLINC/graphql-to-typescript](https://github.com/3VLINC/graphql-to-typescript) | 29 | `mocha "dist/**/*.test.js"` | 
| [coderfox/clover](https://github.com/coderfox/clover) | 29 | `nyc mocha` | 
| [georgehanson/Vue-Form-Components](https://github.com/georgehanson/Vue-Form-Components) | 29 | `mocha-webpack --webpack-config="webpack.test.config.js" --require="tests/setup.ts" tests/**/*.spec.ts` | 
| [masvis/angular4-hal](https://github.com/masvis/angular4-hal) | 29 | `mocha -r ts-node/register --config=test/test-config.json test/*.test.ts` | 
| [aleixmorgadas/nem-library-ts](https://github.com/aleixmorgadas/nem-library-ts) | 29 | `mocha --ui bdd --recursive ./dist/test ./dist/integration_test --timeout 60000` | 
| [TomShacham/http4js](https://github.com/TomShacham/http4js) | 29 | `tsc; mocha --require ts-node/register 'src/{test,ssl}/**/*.ts'` | 
| [patrimart/monadness-js](https://github.com/patrimart/monadness-js) | 29 | `./node_modules/.bin/istanbul cover ./node_modules/mocha/bin/_mocha --report lcovonly -- -R spec && cat ./coverage/lcov.info | ./node_modules/coveralls/bin/coveralls.js && rm -rf ./coverage` | 
| [glixlur/jsx-dom](https://github.com/glixlur/jsx-dom) | 28 | `nyc --reporter=html mocha test/test.tsx --require test/register` | 
| [jan-molak/tiny-types](https://github.com/jan-molak/tiny-types) | 28 | `nyc --report-dir ./reports/coverage mocha --opts ./mocha.opts 'spec/**/*.spec.*'` | 
| [larshp/abaplint](https://github.com/larshp/abaplint) | 28 | `mocha --recursive --reporter progress build/test` | 