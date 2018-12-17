# Find Repos in TypeScript Tested using Mocha

The list was updated at 01:55:29 12/17/18 PST

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 65786 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 16270 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 10982 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 9721 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 6984 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 6163 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 5286 | `npm run mocha` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4588 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4380 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 3883 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3378 | `mocha --opts mocha.opts` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2826 | `mocha` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2742 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 2725 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2428 | `mocha 'test/**/*.ts'` | 
| [electron-userland/electron-forge](https://github.com/electron-userland/electron-forge) | 2405 | `cross-env TS_NODE_FILES=true yarn run mocha './tools/test-globber.ts' --opts mocha.opts` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2202 | `mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1863 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1862 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1791 | `mocha` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1742 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1414 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1374 | `nyc -x '' mocha` | 
| [gamestdio/colyseus](https://github.com/gamestdio/colyseus) | 1363 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 1250 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1240 | `mocha --opts mocha.opts` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1233 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [funkia/list](https://github.com/funkia/list) | 1221 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [shanalikhan/code-settings-sync](https://github.com/shanalikhan/code-settings-sync) | 1206 | `npm run tslint-check && tsc -p ./ && mocha --recursive "./out/test/**/*.js"` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1188 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [cherow/cherow](https://github.com/cherow/cherow) | 1181 | `cross-env TS_NODE_PROJECT="test/tsconfig.json" mocha test/**/*.ts -c -R progress -r ts-node/register -r source-map-support/register --recursive --globals expect` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1116 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [google/clasp](https://github.com/google/clasp) | 1094 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1091 | `nyc --reporter=html --reporter=text mocha` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 1040 | `tsc -p ./ && mocha` | 
| [itchio/itch](https://github.com/itchio/itch) | 967 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 930 | `mocha --opts test/mocha.opts` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 902 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 862 | `mocha bin/tests/test.js` | 
| [netgusto/nodebook](https://github.com/netgusto/nodebook) | 767 | `mocha test/backend` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 733 | `yarn run lint && yarn run test:mocha` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 731 | `mocha --compilers ts:ts-node/register test/*.js || true` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 711 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 702 | `mocha` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 700 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 673 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 665 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 657 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 647 | `mocha --recursive` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 611 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 601 | `mocha "out/**/*.spec.js" -s 0` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 590 | `npm run lint && npm run mocha` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 586 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [googleapis/google-auth-library-nodejs](https://github.com/googleapis/google-auth-library-nodejs) | 558 | `nyc mocha build/test` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 555 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 551 | `mocha test` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 551 | `mocha` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 544 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 540 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 536 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 536 | `mocha --opts test/mocha.opts dist/test` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 526 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 524 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 482 | `mocha --opts mocha.opts` | 
| [dsherret/ts-simple-ast](https://github.com/dsherret/ts-simple-ast) | 474 | `cross-env TS_NODE_COMPILER="ttypescript" TS_NODE_TRANSPILE_ONLY="true" mocha --opts mocha.opts --grep @performance --invert` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 467 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 465 | `cross-env NODE_ENV=tsoa_test mocha **/*.spec.ts --exit --compilers ts:ts-node/register` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 463 | `npm run build && mocha` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 462 | `mocha --opts mocha.opts` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 452 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 447 | `npm run mocha` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 444 | `_mocha --` | 
| [Romakita/ts-express-decorators](https://github.com/Romakita/ts-express-decorators) | 442 | `npm run clean && npm run tsc && npm run tslint && cross-env NODE_ENV=test nyc --reporter=html --reporter=text _mocha --recursive` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 435 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 434 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 416 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 414 | `cd test && mocha -r ts-node/register *.ts` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 398 | `mocha test/unit` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 396 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 393 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 391 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 384 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [R-js/libRmath.js](https://github.com/R-js/libRmath.js) | 377 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 359 | `mocha` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 349 | `npm run build && mocha` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 345 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 336 | `tsc && mocha test && yarn lint` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 335 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 333 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 319 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [Microsoft/node-pty](https://github.com/Microsoft/node-pty) | 312 | `cross-env NODE_ENV=test mocha -R spec --exit lib/*.test.js` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 309 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 301 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 295 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 289 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 289 | `mocha` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 285 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 284 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 283 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts view/test/test-heightmap.ts` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 282 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 281 | `mocha` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 276 | `mocha lib/test` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 273 | `mocha` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 272 | `mocha --compilers js:babel-register test/**/*.js` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 269 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 262 | `mocha src/**/*.spec.ts` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 250 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 247 | `mocha "test/**/*.spec.ts"` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 245 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [dubzzz/fast-check](https://github.com/dubzzz/fast-check) | 244 | `npm run build && nyc mocha "test/unit/**/*.spec.ts"` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 238 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 237 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 237 | `tsc && mocha dist/**/*.spec.js` | 
| [AmirTugi/tea-school](https://github.com/AmirTugi/tea-school) | 235 | `npx ts-mocha ./src/tests/**.ts` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 235 | `tsc && mocha` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 225 | `nyc --reporter html mocha` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 224 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 221 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 221 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 214 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 213 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 212 | `mocha-webpack "src/**/*.ts"` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 209 | `mocha test` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 204 | `mocha dist/test.js` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 201 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 200 | `mocha -R spec test/integration` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 199 | `cross-env NODE_ENV=test mocha` | 
| [Zarel/Pokemon-Showdown-Client](https://github.com/Zarel/Pokemon-Showdown-Client) | 198 | `eslint --config=.eslintrc.js --cache --cache-file=eslint-cache/base js/ data/ && eslint --config=build-tools/.eslintrc.js --cache --cache-file=eslint-cache/build build-tools/update build-tools/build-indexes && tslint --project . && tsc && node build && mocha` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 197 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [R-js/blasjs](https://github.com/R-js/blasjs) | 195 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [bmewburn/intelephense](https://github.com/bmewburn/intelephense) | 192 | `mocha -r ts-node/register test/*.ts` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 187 | `mocha js` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 187 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 185 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 185 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 183 | `nyc mocha --recursive test/**/*.ts` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 182 | `cd test && mocha -r ts-node/register *.ts` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 178 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 178 | `mocha lib/spec/core` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 174 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 174 | `npm run build && npm run mocha` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 173 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 172 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 171 | `npm run lint && npm run mocha` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 167 | `tsc && cd dist && mocha` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 166 | `npm run clean && npm run build && npm run lint && mocha` | 
| [emmanueltouzery/prelude-ts](https://github.com/emmanueltouzery/prelude-ts) | 162 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [Chinachu/Mirakurun](https://github.com/Chinachu/Mirakurun) | 158 | `mocha --exit test/*.spec.js` | 
| [kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | 157 | `nyc mocha` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 156 | `gulp compile && mocha --timeout 10000 -u tdd ./out/tests/` | 
| [nodejs/llhttp](https://github.com/nodejs/llhttp) | 155 | `npm run mocha && npm run lint` | 
| [p-society/typeracer-cli](https://github.com/p-society/typeracer-cli) | 155 | `mocha --no-deprecation --timeout 10000 --require ts-node/register **/*.spec.ts` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 153 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 152 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [hydux/hydux](https://github.com/hydux/hydux) | 149 | `npm run mocha -- "src/test/unit/*.test.ts"` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 147 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 144 | `tsc && mocha` | 
| [calidion/vig](https://github.com/calidion/vig) | 144 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 140 | `gulp compile && mocha` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 140 | `mocha lib/test` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 139 | `mocha -r ts-node/register test/*.ts` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 128 | `npm run-script build && mocha --opts test/mocha.opts build/test/config.js build/test` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 128 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [cartant/rxjs-marbles](https://github.com/cartant/rxjs-marbles) | 126 | `yarn run lint && yarn run test:build && cross-env FAILING=0 yarn run test:ava && cross-env FAILING=0 yarn run test:jasmine && cross-env FAILING=0 yarn run test:jasmine-angular && cross-env FAILING=0 yarn run test:jest && cross-env FAILING=0 yarn run test:mocha && cross-env FAILING=0 yarn run test:tape` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 126 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [rtfeldman/node-elm-compiler](https://github.com/rtfeldman/node-elm-compiler) | 126 | `rm -rf test/fixtures/elm-stuff & mocha test/**/*.ts --require ts-node/register --watch-extensions ts` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 125 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 125 | `nyc --reporter=html --reporter=text mocha` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 124 | `istanbul test -- _mocha` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 124 | `mocha --require espower-typescript/guess "test/**/*.test.ts"` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 124 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 123 | `mocha --require source-map-support/register dist/test` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 122 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [prh/prh](https://github.com/prh/prh) | 122 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 121 | `mocha test` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 121 | `mocha` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 120 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 126 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [rtfeldman/node-elm-compiler](https://github.com/rtfeldman/node-elm-compiler) | 126 | `rm -rf test/fixtures/elm-stuff & mocha test/**/*.ts --require ts-node/register --watch-extensions ts` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 125 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 125 | `nyc --reporter=html --reporter=text mocha` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 124 | `istanbul test -- _mocha` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 124 | `mocha --require espower-typescript/guess "test/**/*.test.ts"` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 124 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 123 | `mocha --require source-map-support/register dist/test` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 122 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [prh/prh](https://github.com/prh/prh) | 122 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 121 | `mocha test` | 
| [Soluto/graphql-to-mongodb](https://github.com/Soluto/graphql-to-mongodb) | 121 | `ts-mocha tests/**/*.spec.ts` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 121 | `mocha` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 120 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 120 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 120 | `mocha --timeout 10000` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 119 | `rimraf ./build && tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 60000 ./build/compiled/test` | 
| [gamestdio/colyseus.js](https://github.com/gamestdio/colyseus.js) | 119 | `mocha test/*.ts --require ts-node/register` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 118 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 116 | `cross-env NODE_ENV=test mocha --exit` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 114 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [VirgilSecurity/demo-twilio-chat-js](https://github.com/VirgilSecurity/demo-twilio-chat-js) | 113 | `mocha --timeout 5000 -r ts-node/register -r tsconfig-paths/register ./api/tests/*.test.ts` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 113 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [nomiclabs/buidler](https://github.com/nomiclabs/buidler) | 113 | `nyc mocha` | 
| [dsherret/ts-nameof](https://github.com/dsherret/ts-nameof) | 113 | `yarn run --silent copy-test-files && nyc --reporter=lcov mocha --opts mocha.opts` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 110 | `mocha` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 109 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 108 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 108 | `node_modules/.bin/nyc npm run mocha` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 107 | `mocha --full-trace tests/test.js  --reporter mocha-multi-reporters` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 107 | `mocha --recursive -t 4000` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 107 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 106 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 106 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 106 | `webpack && mocha-phantomjs test/index.html` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 105 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [Microsoft/typescript-tslint-plugin](https://github.com/Microsoft/typescript-tslint-plugin) | 105 | `mocha ./out/**/*.test.js --slow 2000 --timeout 10000` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 105 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 105 | `mocha -R spec dist/test/**/*.js` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 105 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 104 | `npm-run-all build test:mocha test:coverage lint` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 102 | `mocha --compilers ts:ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 102 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 102 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 102 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [Esri/react-arcgis](https://github.com/Esri/react-arcgis) | 101 | `nyc mocha` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 100 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 100 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 100 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 99 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 99 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 98 | `tsc; mocha --recursive lib/ test/runner` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 98 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 97 | `mocha` | 
| [nodejs/llparse](https://github.com/nodejs/llparse) | 97 | `npm run mocha && npm run lint` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 97 | `mocha ./spec/*.js` | 
| [wildbit/postmark.js](https://github.com/wildbit/postmark.js) | 97 | `node_modules/mocha/bin/mocha --timeout 10000 --retries 1 -r ts-node/register test/**/*test.ts` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 97 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 96 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [nucleojs/nucleo](https://github.com/nucleojs/nucleo) | 96 | `mocha -r ts-node/register` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 93 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 93 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 93 | `nyc npm run _mocha` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 93 | `node node_modules/mocha/bin/mocha` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 93 | `mocha test/* --timeout 500000` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 91 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 91 | `mocha` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 90 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 90 | `mocha test/ --recursive` | 
| [levjj/esverify](https://github.com/levjj/esverify) | 90 | `TS_NODE_TRANSPILE_ONLY=true mocha -r ts-node/register tests/*.ts` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 89 | `mocha ./dist/test --recursive` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 89 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register 'test/**/*.ts'` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 89 | `npm run lint && npm run prettier && npm run mocha` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 88 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 87 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 86 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 83 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 82 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [vrimar/construct-ui](https://github.com/vrimar/construct-ui) | 81 | `cross-env TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 81 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 81 | `mocha` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 80 | `mocha --require ts-node/register test/**/*.ts` | 
| [vrimar/construct-ui](https://github.com/vrimar/construct-ui) | 81 | `cross-env TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 81 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 81 | `mocha` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 80 | `mocha --require ts-node/register test/**/*.ts` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 79 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 78 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 78 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 78 | `mocha --ui tdd out/test/extension.test.js` | 
| [CityOfZion/neo-js](https://github.com/CityOfZion/neo-js) | 77 | `mocha --reporter spec` | 
| [teambition/ReactiveDB](https://github.com/teambition/ReactiveDB) | 76 | `npm run lint && NODE_ENV=test tman --mocha spec-js/test/run.js` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 76 | `tsc && mocha "dist/test/**/*.js" ` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 76 | `npm run lint && npm run mocha` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 75 | `nyc mocha --recursive test/**/*.ts` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 75 | `mocha --compilers js:babel-core/register --recursive` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 74 | `mocha -r ./src/test/common/setup.ts ./lib/src/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 74 | `nyc mocha build/test` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 74 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 74 | `npm run lint && nyc mocha` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 73 | `nyc mocha` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 73 | `TS_NODE_PROJECT=test/tsconfig.json mocha` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 72 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 72 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 72 | `mocha -r ts-node/register 'test/main.js'` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 72 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 71 | `mocha -u tdd ./out/tests/` | 
| [bpatrik/pigallery2](https://github.com/bpatrik/pigallery2) | 71 | `ng test && mocha --recursive test/backend/unit && mocha --recursive test/backend/integration  && mocha --recursive test/common/unit ` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 71 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 70 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 70 | `mocha out/**/*.spec.js` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 70 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 70 | `TS_NODE_FILES=true mocha --opts src/test/mocha.opts "src/test/test*.ts"` | 
| [googleapis/nodejs-datastore](https://github.com/googleapis/nodejs-datastore) | 70 | `nyc mocha build/test` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 69 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 69 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 68 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 68 | `nyc mocha lib/**/*Test.js` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 68 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 67 | `npm run compile && mocha && npm run lint` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 67 | `mocha -r ts-node/register test/*.ts` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 67 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 65 | `nyc mocha` | 
| [puzzle-js/PuzzleJs](https://github.com/puzzle-js/PuzzleJs) | 64 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 64 | `nyc mocha build/test` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 63 | `mocha .tmp/spec/index.spec.js` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 63 | `mocha --timeout 10000 --slow 2500 tests/unittests/**/*.spec.js tests/functional-test-cases.js` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 62 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 62 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 62 | `mocha 'lib/**/__tests__/*.js'` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 62 | `mocha dist/test/*.js` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 61 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 61 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 61 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [roblox-ts/roblox-ts](https://github.com/roblox-ts/roblox-ts) | 61 | `nyc --reporter=html mocha --timeout 0 --require ts-node/register --require source-map-support/register --recursive src/test.ts && lua tests/spec.lua` | 
| [wix/rawss](https://github.com/wix/rawss) | 60 | `mocha` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 60 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 60 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 59 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 59 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 59 | `mocha --opts spec/mocha.opts spec/**/*-spec.ts` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 58 | `mocha build/tests/index.js` | 
| [ethereumjs/rlp](https://github.com/ethereumjs/rlp) | 58 | `npm run lint && mocha --reporter spec --require ts-node/register test/index.ts` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 58 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd ./out/test/extension.test.js` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 58 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 57 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 57 | `nyc mocha --opts .mocha.opts` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 57 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 57 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 56 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 55 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 55 | `mocha --timeout 30000 test/**/*.js` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 55 | `mocha --recursive` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 55 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [DhyanaChina/koa2-typescript-guide](https://github.com/DhyanaChina/koa2-typescript-guide) | 54 | `mocha` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 54 | `npm run build && npm run mocha` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 54 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 53 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 53 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 53 | `mocha` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 53 | `mocha` | 
| [nhabuiduc/react-filter-box](https://github.com/nhabuiduc/react-filter-box) | 53 | `node --max-old-space-size=16000 ./node_modules/.bin/mocha-webpack --require ignore-styles -r jsdom-global/register --webpack-config webpack.test.config.js --watch "./test/**/*.ts"` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 53 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 53 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 52 | `NODE_ENV=test nyc mocha` | 
| [AlCalzone/node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 52 | `node_modules/.bin/mocha --watch` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 52 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 52 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 52 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 51 | `mocha --ui qunit` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 51 | `mocha` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 51 | `NODE_ENV=test nyc mocha` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 51 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 51 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [DhyanaChina/todo-live](https://github.com/DhyanaChina/todo-live) | 51 | `mocha` | 
| [wearetheledger/fabric-node-chaincode-utils](https://github.com/wearetheledger/fabric-node-chaincode-utils) | 51 | `mocha -r ts-node/register test/**/*.spec.ts --reporter spec` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 50 | `npm run compile && mocha` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [voodooattack/serialism](https://github.com/voodooattack/serialism) | 50 | `nyc mocha --expose-gc --ui mocha-typescript test/test_**.ts` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 50 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 50 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 49 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 49 | `nyc mocha` | 
| [mono/TsToCSharp](https://github.com/mono/TsToCSharp) | 49 | `npm run lint && mocha  ./dist/TsToCSharpTests.js` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 48 | `cross-env NODE_ENV=test mocha` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 48 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 48 | `mocha test/*.js` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 48 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 48 | `tsc --version && tsc && mocha out/test` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 48 | `mocha --opts test/mocha.opts` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 48 | `nyc mocha` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 47 | `mocha --opts config/mocha.opts` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 47 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 47 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 47 | `npm run compile && mocha && npm run lint` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 47 | `mocha --compilers ts:ts-node/register --recursive` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [CommandBlockLogic/spu](https://github.com/CommandBlockLogic/spu) | 47 | `mocha --require espower-typescript/guess "./src/test/**/*.ts"` | 
| [teppeis/closure-ts](https://github.com/teppeis/closure-ts) | 47 | `npm-run-all --aggregate-output -p lint:ts build -p lint:js mocha` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 47 | `nyc mocha --opts test/mocha.opts` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 46 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 46 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 46 | `mocha --opts mocha.opts --watch` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [ethereumjs/ethereumjs-blockstream](https://github.com/ethereumjs/ethereumjs-blockstream) | 46 | `mocha --require ts-node/register tests/**/*.ts` | 
| [sourcegraph/browser-extensions](https://github.com/sourcegraph/browser-extensions) | 46 | `mocha --require ts-node/register --watch --watch-extensions ts './src/**/*.test.ts?(x)'` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 46 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 46 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [balmbees/dynamo-types](https://github.com/balmbees/dynamo-types) | 46 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 45 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [lukeautry/ts-app](https://github.com/lukeautry/ts-app) | 45 | `cross-env TS_NODE_PROJECT=./api/tsconfig.json mocha -t 15000 -r ts-node/register "./api/**/*.spec.ts"` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 45 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [hg-pyun/iterize](https://github.com/hg-pyun/iterize) | 45 | `mocha --recursive ./test/*.ts --require ts-node/register` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 45 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [rcjsuen/dockerfile-language-server-nodejs](https://github.com/rcjsuen/dockerfile-language-server-nodejs) | 44 | `mocha out/test` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 44 | `mocha -R spec ./test` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 44 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 43 | `npm run lint && mocha dist/spec` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 43 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [googleapis/nodejs-spanner](https://github.com/googleapis/nodejs-spanner) | 43 | `nyc mocha build/test` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 43 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 43 | `mocha` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 43 | `mocha test` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 43 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 43 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 43 | `mocha --reporter spec` | 
| [ashleydavis/grademark](https://github.com/ashleydavis/grademark) | 43 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [adumont/tplink-cloud-api](https://github.com/adumont/tplink-cloud-api) | 42 | `mocha -r ts-node/register -p tsconfig.json lib/**/*.spec.ts` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 42 | `npm run prettier && npm run lint && npm run mocha` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 42 | `mocha` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 42 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [seansfkelley/synology-download-manager](https://github.com/seansfkelley/synology-download-manager) | 42 | `TS_NODE_PROJECT=test/tsconfig-test.json mocha --require ts-node/register 'test/**/*.{ts,tsx}'` | 
| [Pushwoosh/web-push-notifications](https://github.com/Pushwoosh/web-push-notifications) | 42 | `mocha` | 
| [Lusito/forget-me-not](https://github.com/Lusito/forget-me-not) | 42 | `nyc mocha --require source-map-support/register --require ts-node/register test/**/*.ts` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 41 | `mocha --opts cli-test-mocha.opts` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 41 | `mocha out/{,**/}*.spec.js -s 0` | 
| [ryu1kn/vscode-partial-diff](https://github.com/ryu1kn/vscode-partial-diff) | 41 | `mocha --opts cli-test-mocha.opts` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 41 | `mocha out/{,**/}*.spec.js -s 0` | 
| [ethereum-ts/evm-ts](https://github.com/ethereum-ts/evm-ts) | 41 | `yarn lint && yarn test:mocha` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 41 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 41 | `tsc && mocha build/test` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 41 | `mocha index.test.js` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 41 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 41 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 40 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 40 | `node_modules/.bin/mocha` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 40 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 40 | `mocha && npm run aplus` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 40 | `cross-env NODE_ENV=test mocha test/**/*.ts` | 
| [just-animate/just-curves](https://github.com/just-animate/just-curves) | 40 | `node_modules/.bin/mocha --require ts-node/register --reporter spec ./tests/**/**.ts` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 40 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 39 | `tsc && npm run lint && mocha` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 39 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [stephenmartindale/kgs-leben](https://github.com/stephenmartindale/kgs-leben) | 39 | `gulp build:tests && mocha --timeout 1000 .build/tests.js` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 39 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 39 | `mocha --recursive` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 39 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 39 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [webix-hub/webix-jet](https://github.com/webix-hub/webix-jet) | 39 | `webpack && phantomjs node_modules/mocha-phantomjs-core/mocha-phantomjs-core.js tests/index.html spec` | 
| [aurelia/bundler](https://github.com/aurelia/bundler) | 39 | `mocha --reporter spec --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 38 | `tsc && mocha dist/**/*.spec.js` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 38 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 37 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 37 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 37 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 37 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 36 | `mocha --opts ./mocha.opts` | 
| [Polymer/polymer-linter](https://github.com/Polymer/polymer-linter) | 36 | `npm run build && mocha && npm run lint` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 36 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [utopian-io/api.utopian.io](https://github.com/utopian-io/api.utopian.io) | 36 | `cross-env NODE_ENV=test npx mocha --ui bdd --reporter spec --colors --recursive -r ts-node/register tests/index.ts` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 36 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [paralin/grpc-bus](https://github.com/paralin/grpc-bus) | 36 | `npm run lint && npm run mocha` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 36 | `npm run mocha && npm run lint` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 35 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [fyndme/messenger-bot-tester](https://github.com/fyndme/messenger-bot-tester) | 35 | `mocha ./test-build` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 35 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 35 | `mocha` | 
| [agea/CmisJS](https://github.com/agea/CmisJS) | 35 | `tsc && mocha dist/**/*.spec.js` | 
| [Pravez/ReImproveJS](https://github.com/Pravez/ReImproveJS) | 35 | `mocha --reporter spec --compilers ts:ts-node/register 'test/*.spec.ts' --timeout 120000` | 
| [gcanti/hyper-ts](https://github.com/gcanti/hyper-ts) | 35 | `npm run prettier && npm run lint && npm run typings-checker && npm run mocha` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 35 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [ste-vg/pop.svg](https://github.com/ste-vg/pop.svg) | 35 | `nyc mocha --require ./mocha.config.js -r ts-node/register 'src/**/*.spec.ts'  --exit --recursive --timeout 10000` | 
| [infinum/mobx-collection-store](https://github.com/infinum/mobx-collection-store) | 35 | `NODE_ENV=test nyc mocha` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 35 | `tsc && mocha spec/` | 
| [secret-tech/backend-token-wallets](https://github.com/secret-tech/backend-token-wallets) | 35 | `mocha -r ts-node/register -r test/prepare.ts src/**/*.spec.ts` | 
| [Jiasm/typescript-example](https://github.com/Jiasm/typescript-example) | 34 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 34 | `mocha test/*.spec.ts` | 
| [Draccoz/twc](https://github.com/Draccoz/twc) | 34 | `npm run lint && mocha --require ts-node/register --ui bdd tests/tests.spec.ts` | 
| [davetemplin/web-request](https://github.com/davetemplin/web-request) | 34 | `mocha` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 34 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [tuzhanai/captcha](https://github.com/tuzhanai/captcha) | 34 | `mocha -b --require ts-node/register --require source-map-support/register --recursive --exit src/test.ts` | 
| [forthright/vile](https://github.com/forthright/vile) | 34 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [supergraphql/supergraph](https://github.com/supergraphql/supergraph) | 34 | `nyc mocha ./dist/**/*.spec.js` | 
| [mixi-inc/css-semdiff](https://github.com/mixi-inc/css-semdiff) | 33 | `mocha --opts mocha.opts './dist/**/*.test.js'` | 
| [tsframework/ts-framework](https://github.com/tsframework/ts-framework) | 33 | `mocha build-test --recursive` | 
| [josephg/statecraft](https://github.com/josephg/statecraft) | 33 | `mocha -r ts-node/register test/*.ts` | 
| [userpixel/typescript](https://github.com/userpixel/typescript) | 33 | `mocha test` | 
| [qtumproject/qtumjs](https://github.com/qtumproject/qtumjs) | 33 | `mocha  lib/*_test.js` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 33 | `mocha --recursive "dist/**/*.test.js"` | 
| [mrmlnc/vscode-stylefmt](https://github.com/mrmlnc/vscode-stylefmt) | 32 | `mocha out/**/*.spec.js -s 0` | 
| [Azure/oav](https://github.com/Azure/oav) | 32 | `npm run tsc && npm run tslint && nyc mocha ./test/**/*.ts -r ts-node/register -t 10000 --reporter mocha-junit-reporter --reporter spec` | 
| [NikitchenkoSergey/scheme-designer](https://github.com/NikitchenkoSergey/scheme-designer) | 32 | `mocha` | 
| [woutervh-/typescript-is](https://github.com/woutervh-/typescript-is) | 32 | `ttsc --project tsconfig-test.json && mocha` | 
| [acrazing/mobx-sync](https://github.com/acrazing/mobx-sync) | 32 | `mocha --require ts-node/register --slow 1000 ./src/**/*.spec.ts` | 
| [davetemplin/async-parallel](https://github.com/davetemplin/async-parallel) | 32 | `mocha` | 
| [leizongmin/leizm-web](https://github.com/leizongmin/leizm-web) | 32 | `npm run format && mocha --require ts-node/register --exit "src/test/**/*.ts"` | 
| [fsahmad/typescript-uml](https://github.com/fsahmad/typescript-uml) | 32 | `npm run build && mocha --compilers ts:ts-node/register --recursive 'src/**/*-spec.ts'` | 
| [igorzg/typeix](https://github.com/igorzg/typeix) | 32 | `npm run compile && mocha build/tests/ --debug --full-trace` | 
| [mulesoft-labs/yaml-ast-parser](https://github.com/mulesoft-labs/yaml-ast-parser) | 32 | `npm run build && mocha --ui tdd dist/test` | 
| [GoodgameStudios/RobotlegsJS](https://github.com/GoodgameStudios/RobotlegsJS) | 32 | `nyc mocha` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 32 | `tsc -p .tsconfig.test.json && mocha` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 32 | `atool-test-mocha ./src/**/*-test.js` | 
| [tbluemel/rtf.js](https://github.com/tbluemel/rtf.js) | 32 | `mocha test/test.js` | 
| [siegebell/vsc-prettify-symbols-mode](https://github.com/siegebell/vsc-prettify-symbols-mode) | 32 | `tsc -p ./ && mocha -u tdd ./out/test` | 
| [Rich-Harris/port-authority](https://github.com/Rich-Harris/port-authority) | 32 | `mocha --opts mocha.opts` | 
| [aleixmorgadas/nem-library-ts](https://github.com/aleixmorgadas/nem-library-ts) | 32 | `mocha --ui bdd --recursive ./dist/test ./dist/integration_test --timeout 60000` | 
| [vrudikov/typescript-rest-boilerplate](https://github.com/vrudikov/typescript-rest-boilerplate) | 32 | `cross-env NODE_ENV=test mocha` | 
| [glixlur/jsx-dom](https://github.com/glixlur/jsx-dom) | 31 | `nyc --reporter=html mocha test/test.tsx --require test/register` | 
| [creeperyang/id3-parser](https://github.com/creeperyang/id3-parser) | 31 | `TS_NODE_PROJECT='test/tsconfig.json' mocha --require ts-node/register 'test/*.spec.ts' --reporter dot` | 
| [ForbesLindesay/barrage](https://github.com/ForbesLindesay/barrage) | 31 | `mocha -R spec lib/test.js` | 
| [RocketChat/Rocket.Chat.js.SDK](https://github.com/RocketChat/Rocket.Chat.js.SDK) | 31 | `nyc mocha './src/lib/**/*.spec.ts'` | 
| [nemtech/nem2-sdk-typescript-javascript](https://github.com/nemtech/nem2-sdk-typescript-javascript) | 31 | `mocha --ui bdd --recursive ./dist/test --timeout 90000` | 
| [pokemongo-dev-contrib/pokemongo-json-pokedex](https://github.com/pokemongo-dev-contrib/pokemongo-json-pokedex) | 31 | `mocha --recursive --compilers ts:ts-node/register,ts:tsconfig-paths/register test/*.ts test/**/*.ts` | 
| [ProjectOpenSea/opensea-js](https://github.com/ProjectOpenSea/opensea-js) | 30 | `./node_modules/.bin/mocha test/*.ts --require ts-node/register --timeout 10000` | 
| [typeorm/typescript-example](https://github.com/typeorm/typescript-example) | 30 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [lebinh/cloudflare-workers](https://github.com/lebinh/cloudflare-workers) | 30 | `mocha -r ts-node/register 'tests/**/*_test.ts'` | 
| [AsynkronIT/protoactor-js](https://github.com/AsynkronIT/protoactor-js) | 30 | `mocha --opts test/mocha.opts -w` | 
| [OpenFinanceIO/smart-securities-standard](https://github.com/OpenFinanceIO/smart-securities-standard) | 30 | `tsc -p tsconfig.test.json && mocha dist/test/*.spec.js src/` | 