# Find Repos in TypeScript Tested using Mocha

The list was updated at 00:43:52 10/16/18 PDT

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 61860 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 15246 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 9374 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec --require 'node_modules/reflect-metadata/Reflect.js'` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 8681 | `tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [sveltejs/svelte](https://github.com/sveltejs/svelte) | 8142 | `mocha --opts mocha.opts && agadoo shared.js` | 
| [googleapis/google-api-nodejs-client](https://github.com/googleapis/google-api-nodejs-client) | 6851 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 5834 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 4889 | `npm run mocha` | 
| [Microsoft/azuredatastudio](https://github.com/Microsoft/azuredatastudio) | 4443 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 4071 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3302 | `mocha --opts mocha.opts` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2756 | `mocha` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 2647 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2452 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2411 | `mocha 'test/**/*.ts'` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 2214 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 2037 | `./node_modules/.bin/mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1809 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1790 | `mocha` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1760 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1673 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1343 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1283 | `nyc -x '' mocha` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1231 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [gamestdio/colyseus](https://github.com/gamestdio/colyseus) | 1209 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [funkia/list](https://github.com/funkia/list) | 1179 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1130 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [watson-developer-cloud/node-sdk](https://github.com/watson-developer-cloud/node-sdk) | 1125 | `nyc mocha test/unit/ test/integration/ && nyc report --reporter=html` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1117 | `mocha --opts mocha.opts` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1078 | `nyc --reporter=html --reporter=text mocha` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1054 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 993 | `tsc -p ./ && mocha` | 
| [itchio/itch](https://github.com/itchio/itch) | 925 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 910 | `mocha --opts test/mocha.opts` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 899 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [google/clasp](https://github.com/google/clasp) | 893 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 860 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 775 | `mocha bin/tests/test.js` | 
| [burtonator/polar-bookshelf](https://github.com/burtonator/polar-bookshelf) | 751 | `mocha-parallel-tests --timeout 10000 --max-parallel=1 --exit --recursive web/js/**/*Test.js` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 720 | `yarn run lint && yarn run test:mocha` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 704 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 673 | `mocha` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 664 | `mocha --compilers ts:ts-node/register test/*.js || true` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 656 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 644 | `mocha --recursive` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 639 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 627 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 623 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 598 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 586 | `npm run lint && npm run mocha` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 577 | `mocha "out/**/*.spec.js" -s 0` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 544 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 544 | `mocha` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 532 | `mocha --opts test/mocha.opts dist/test` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 530 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [brannondorsey/chattervox](https://github.com/brannondorsey/chattervox) | 527 | `mocha test` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 523 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [pgilad/leasot](https://github.com/pgilad/leasot) | 516 | `mocha --require ts-node/register -R spec './tests/*.ts'` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 500 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 487 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 473 | `mocha --opts mocha.opts` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 464 | `npm run build && mocha` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 458 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 443 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 441 | `_mocha --` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 429 | `mocha --opts mocha.opts` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 422 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 353 | `cd test && mocha -r ts-node/register *.ts` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 341 | `npm run build && mocha` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 323 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 321 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 296 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 353 | `cd test && mocha -r ts-node/register *.ts` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 347 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 341 | `npm run build && mocha` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 323 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 321 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 296 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 292 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 289 | `mocha` | 
| [zlq4863947/triangular-arbitrage](https://github.com/zlq4863947/triangular-arbitrage) | 279 | `cross-env NODE_ENV=test mocha dist/**/*.test.js --timeout 5000 --require intelli-espower-loader` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 279 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [Microsoft/node-pty](https://github.com/Microsoft/node-pty) | 279 | `cross-env NODE_ENV=test mocha -R spec --exit lib/*.test.js` | 
| [cdonohue/polychrome](https://github.com/cdonohue/polychrome) | 270 | `mocha --compilers js:babel-register test/**/*.js` | 
| [GoogleChrome/chrome-launcher](https://github.com/GoogleChrome/chrome-launcher) | 269 | `mocha --require ts-node/register --reporter=dot test/**/*-test.ts --timeout=10000` | 
| [spiffcode/ghedit](https://github.com/spiffcode/ghedit) | 264 | `mocha` | 
| [SweetIQ/schemats](https://github.com/SweetIQ/schemats) | 264 | `npm run lint && npm run build && npm run dependency-check && mocha` | 
| [mgechev/aspect.js](https://github.com/mgechev/aspect.js) | 263 | `tsc && mocha -R nyan ./dist/test/**/*.spec.js` | 
| [worr/node-imdb-api](https://github.com/worr/node-imdb-api) | 262 | `nyc --require ts-node/register --reporter=lcov node_modules/mocha/bin/mocha test/*.ts` | 
| [Canner/apollo-link-firebase](https://github.com/Canner/apollo-link-firebase) | 260 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --timeout 10000 --compilers ts:ts-node/register --recursive --exit "test/**/*.spec.ts"` | 
| [cbowdon/TsMonad](https://github.com/cbowdon/TsMonad) | 258 | `mocha lib/test` | 
| [albburtsev/bem-cn](https://github.com/albburtsev/bem-cn) | 256 | `mocha src/**/*.spec.ts` | 
| [frankwallis/plugin-typescript](https://github.com/frankwallis/plugin-typescript) | 248 | `mocha --require ./test/environment --timeout 10000 ./test/*.ts` | 
| [cyclejs/react-native](https://github.com/cyclejs/react-native) | 241 | `TS_NODE_PROJECT=test/tsconfig.json mocha test/*.ts --require @huston007/react-native-mock/mock.js --require ts-node/register --recursive` | 
| [whitecolor/yalc](https://github.com/whitecolor/yalc) | 240 | `mocha test` | 
| [SpoonX/wetland](https://github.com/SpoonX/wetland) | 233 | `mocha dist/test/helper dist/test/unit/{*.spec.js,**/*.spec.js} --timeout 15000` | 
| [dividab/tsconfig-paths](https://github.com/dividab/tsconfig-paths) | 233 | `mocha` | 
| [liangzeng/cqrs](https://github.com/liangzeng/cqrs) | 231 | `tsc && mocha` | 
| [duniter/duniter](https://github.com/duniter/duniter) | 226 | `nyc --reporter html mocha` | 
| [codemirror/codemirror.next](https://github.com/codemirror/codemirror.next) | 222 | `mocha -r ts-node/register/transpile-only doc/test/test-*.ts state/test/test-*.ts history/test/test-*.ts rangeset/test/test-rangeset.ts keymap/test/test-*.ts legacy-modes/test/test-*.ts view/test/test-heightmap.ts` | 
| [ReactiveX/rxjs-tslint](https://github.com/ReactiveX/rxjs-tslint) | 215 | `rimraf dist && tsc && mocha -R nyan dist/test --recursive` | 
| [renke/import-sort](https://github.com/renke/import-sort) | 214 | `mocha --require ts-node/register --recursive "packages/*/test/**/*.ts"` | 
| [RisingStack/node-typescript-starter](https://github.com/RisingStack/node-typescript-starter) | 213 | `tsc && mocha dist/**/*.spec.js` | 
| [stardustjs/stardust-core](https://github.com/stardustjs/stardust-core) | 205 | `mocha test` | 
| [Microsoft/vscode-cordova](https://github.com/Microsoft/vscode-cordova) | 204 | `node ./node_modules/mocha/bin/mocha --recursive -u bdd ./out/test/debugger` | 
| [dubzzz/fast-check](https://github.com/dubzzz/fast-check) | 202 | `npm run build && nyc mocha "test/unit/**/*.spec.ts"` | 
| [zekelevu/typeframework](https://github.com/zekelevu/typeframework) | 199 | `mocha -R spec test/integration` | 
| [Polymer/polyserve](https://github.com/Polymer/polyserve) | 197 | `npm run build && mocha && tslint "src/**/*.ts"` | 
| [HerringtonDarkholme/av-ts](https://github.com/HerringtonDarkholme/av-ts) | 194 | `mocha dist/test.js` | 
| [jedmao/eclint](https://github.com/jedmao/eclint) | 193 | `nyc npm run mocha -- --reporter lcov --reporter spec` | 
| [ClickSimply/Nano-SQL](https://github.com/ClickSimply/Nano-SQL) | 189 | `mocha -r ts-node/register tests/index.ts` | 
| [styleguidist/react-docgen-typescript](https://github.com/styleguidist/react-docgen-typescript) | 186 | `tsc && mocha --timeout 10000 ./lib/**/__tests__/**.js` | 
| [JumpFm/jumpfm](https://github.com/JumpFm/jumpfm) | 185 | `mocha js` | 
| [rubenspgcavalcante/webpack-chrome-extension-reloader](https://github.com/rubenspgcavalcante/webpack-chrome-extension-reloader) | 185 | `NODE_ENV=test webpack && mocha dist/tests.js` | 
| [codeaholicguy/wowcup](https://github.com/codeaholicguy/wowcup) | 184 | `nyc mocha --forbid-only "test/**/*.test.ts"` | 
| [thiagobustamante/typescript-rest](https://github.com/thiagobustamante/typescript-rest) | 182 | `cross-env NODE_ENV=test mocha` | 
| [jacobbogers/blasjs](https://github.com/jacobbogers/blasjs) | 181 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [Kononnable/typeorm-model-generator](https://github.com/Kononnable/typeorm-model-generator) | 178 | `istanbul cover ./node_modules/mocha/bin/_mocha dist/test/**/*.test.js  -- -R spec` | 
| [bmewburn/intelephense](https://github.com/bmewburn/intelephense) | 175 | `mocha -r ts-node/register test/*.ts` | 
| [brentlintner/synt](https://github.com/brentlintner/synt) | 171 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [cartant/rxjs-tslint-rules](https://github.com/cartant/rxjs-tslint-rules) | 171 | `yarn run lint && yarn run test:build && yarn run test:mocha && yarn run test:tslint-v5 && yarn run test:tslint-v6 && yarn run test:tslint-v6-compat` | 
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | 170 | `mocha-webpack "src/**/*.ts"` | 
| [funkia/hareactive](https://github.com/funkia/hareactive) | 170 | `nyc mocha --recursive test/**/*.ts` | 
| [staltz/html-looks-like](https://github.com/staltz/html-looks-like) | 170 | `npm run lint && npm run mocha` | 
| [felixfbecker/iterare](https://github.com/felixfbecker/iterare) | 168 | `mocha -r source-map-support/register lib/**/*.test.js` | 
| [Polymer/polymer-analyzer](https://github.com/Polymer/polymer-analyzer) | 167 | `npm run clean && npm run build && npm run lint && mocha` | 
| [ohjames/rxjs-websockets](https://github.com/ohjames/rxjs-websockets) | 165 | `npm run build && npm run mocha` | 
| [fabiandev/ts-runtime](https://github.com/fabiandev/ts-runtime) | 163 | `NODE_ENV=test TS_NODE_CACHE=false ./node_modules/mocha/bin/_mocha` | 
| [FormidableLabs/inspectpack](https://github.com/FormidableLabs/inspectpack) | 163 | `mocha "test/**/*.spec.ts"` | 
| [pnp/office365-cli](https://github.com/pnp/office365-cli) | 162 | `nyc -r=lcov -r=text mocha "dist/**/*.spec.js"` | 
| [microsoftgraph/msgraph-sdk-javascript](https://github.com/microsoftgraph/msgraph-sdk-javascript) | 160 | `mocha lib/spec/core` | 
| [square/babel-codemod](https://github.com/square/babel-codemod) | 156 | `mocha "test/**/*Test.js"` | 
| [drew-y/cliffy](https://github.com/drew-y/cliffy) | 156 | `tsc && cd dist && mocha` | 
| [chenhaozhi/Cpage.js](https://github.com/chenhaozhi/Cpage.js) | 154 | `mocha -r ./node_modules/ts-node/register test/**/*_spec.ts --reporter mochawesome` | 
| [Microsoft/vscode-node-debug](https://github.com/Microsoft/vscode-node-debug) | 149 | `mocha --timeout 10000 -u tdd ./out/tests/` | 
| [jgranstrom/zipson](https://github.com/jgranstrom/zipson) | 147 | `mocha --require ts-node/register --watch-extensions ts 'test/**/*.ts'` | 
| [emmanueltouzery/prelude.ts](https://github.com/emmanueltouzery/prelude.ts) | 145 | `rm tests/apidoc-*; tsc && node ./dist/tests/Comments.js && tsc && ./node_modules/mocha/bin/mocha --throw-deprecation --timeout 60000 ./dist/tests/*.js` | 
| [calidion/vig](https://github.com/calidion/vig) | 142 | `npm run build && nyc --reporter=text --reporter=html --reporter=lcov mocha --bail --compilers ts:ts-node/register --recursive 'test/**/*.test.ts'` | 
| [oclif/cli-ux](https://github.com/oclif/cli-ux) | 139 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [Talento90/typescript-node](https://github.com/Talento90/typescript-node) | 137 | `npm run build && mocha --exit --recursive dist/test/unit` | 
| [nestjs/cqrs](https://github.com/nestjs/cqrs) | 134 | `tsc && mocha` | 
| [Azure/azure-functions-pack](https://github.com/Azure/azure-functions-pack) | 133 | `npm run build && mocha --compilers ts:ts-node/register --recursive test/**/*-spec.ts` | 
| [hydux/hydux](https://github.com/hydux/hydux) | 132 | `npm run mocha -- "src/test/unit/*.test.ts"` | 
| [Commit451/skyhook](https://github.com/Commit451/skyhook) | 132 | `mocha -r ts-node/register test/*.ts` | 
| [rangle/typed-immutable-record](https://github.com/rangle/typed-immutable-record) | 131 | `npm run typings  && npm run lint && nyc npm run mocha` | 
| [Urigo/angular-meteor-base](https://github.com/Urigo/angular-meteor-base) | 131 | `TEST_BROWSER_DRIVER=phantomjs meteor test --driver-package=ardatan:mocha` | 
| [rhysd/neovim-component](https://github.com/rhysd/neovim-component) | 130 | `mocha test/unit/ --exit` | 
| [tomastrajan/ngx-model](https://github.com/tomastrajan/ngx-model) | 129 | `npm run clean && tslint *.ts && npm run format:ci && mocha ./lib/model.test.ts --require ts-node/register` | 
| [implydata/plyql](https://github.com/implydata/plyql) | 129 | `mocha` | 
| [danvk/localturk](https://github.com/danvk/localturk) | 127 | `mocha --require ts-node/register test/**/*.ts` | 
| [Microsoft/vscode-ios-web-debug](https://github.com/Microsoft/vscode-ios-web-debug) | 127 | `node ./node_modules/mocha/bin/mocha --recursive -u tdd ./out/test/` | 
| [nspragg/filehound](https://github.com/nspragg/filehound) | 127 | `mocha -r ts-node/register test/*.ts` | 
| [googlearchive/polylint](https://github.com/googlearchive/polylint) | 125 | `bower install && node_modules/.bin/jshint test && node_modules/.bin/mocha test/test.js` | 
| [TrustWallet/trust-ray](https://github.com/TrustWallet/trust-ray) | 124 | `cross-env NODE_ENV=test mocha --recursive --require ts-node/register 'test/**/*.test.ts' --exit` | 
| [mjhea0/typescript-node-api](https://github.com/mjhea0/typescript-node-api) | 124 | `mocha --reporter spec --compilers ts:ts-node/register 'test/**/*.test.ts'` | 
| [DotJoshJohnson/vscode-xml](https://github.com/DotJoshJohnson/vscode-xml) | 123 | `npm run compile && mocha ./out/test/**/*.js` | 
| [arusanov/avatar-generator](https://github.com/arusanov/avatar-generator) | 122 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [tanepiper/node-bitly](https://github.com/tanepiper/node-bitly) | 122 | `VCR_MODE=cache mocha -r ts-node/register --reporter list src/*.spec.ts` | 
| [interledgerjs/ilp](https://github.com/interledgerjs/ilp) | 121 | `istanbul test -- _mocha` | 
| [Microsoft/vscode-vsce](https://github.com/Microsoft/vscode-vsce) | 121 | `gulp compile && mocha` | 
| [nozer/quill-delta-to-html](https://github.com/nozer/quill-delta-to-html) | 121 | `./node_modules/nyc/bin/nyc.js ./node_modules/mocha/bin/mocha --compilers ts:ts-node/register -b "./test/**/*.ts"  ` | 
| [martysweet/cfn-lint](https://github.com/martysweet/cfn-lint) | 121 | `mocha lib/test` | 
| [ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake) | 119 | `mocha --compilers ts:ts-node/register test/*.ts` | 
| [tfoxy/chrome-promise](https://github.com/tfoxy/chrome-promise) | 119 | `mocha --timeout 10000` | 
| [Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) | 118 | `mocha test` | 
| [Glavin001/graphql-sequelize-crud](https://github.com/Glavin001/graphql-sequelize-crud) | 118 | `mocha --require source-map-support/register dist/test` | 
| [paulcbetts/spawn-rx](https://github.com/paulcbetts/spawn-rx) | 118 | `mocha --compilers ts:ts-node/register ./test/*` | 
| [prh/prh](https://github.com/prh/prh) | 117 | `npm run build && mocha --reporter spec --require intelli-espower-loader` | 
| [pocesar/node-stratum](https://github.com/pocesar/node-stratum) | 115 | `node ./node_modules/typescript/bin/tsc -p tests.json && mocha test` | 
| [AzureAD/azure-activedirectory-library-for-nodejs](https://github.com/AzureAD/azure-activedirectory-library-for-nodejs) | 115 | `npm run tsc && mocha -R spec --ui tdd test` | 
| [VirgilSecurity/demo-twilio-chat-js](https://github.com/VirgilSecurity/demo-twilio-chat-js) | 114 | `mocha --timeout 5000 -r ts-node/register -r tsconfig-paths/register ./api/tests/*.test.ts` | 
| [cartant/rxjs-marbles](https://github.com/cartant/rxjs-marbles) | 114 | `yarn run lint && yarn run test:build && cross-env FAILING=0 yarn run test:ava && cross-env FAILING=0 yarn run test:jasmine && cross-env FAILING=0 yarn run test:jasmine-angular && cross-env FAILING=0 yarn run test:jest && cross-env FAILING=0 yarn run test:mocha && cross-env FAILING=0 yarn run test:tape` | 
| [Half-Shot/matrix-appservice-discord](https://github.com/Half-Shot/matrix-appservice-discord) | 113 | `npm run-script build && mocha --opts test/mocha.opts build/test` | 
| [Microsoft/monaco-languages](https://github.com/Microsoft/monaco-languages) | 113 | `mocha` | 
| [mgechev/ngresizable](https://github.com/mgechev/ngresizable) | 112 | `mocha --require ts-node/register test/**/*.spec.ts --recursive` | 
| [TreeGateway/tree-gateway](https://github.com/TreeGateway/tree-gateway) | 110 | `cross-env NODE_ENV=test mocha --exit` | 
| [championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators) | 109 | `cd test && mocha -r ts-node/register *.ts` | 
| [Urigo/meteor-rxjs](https://github.com/Urigo/meteor-rxjs) | 107 | `cd tests && meteor test --driver-package practicalmeteor:mocha` | 
| [gamestdio/colyseus.js](https://github.com/gamestdio/colyseus.js) | 107 | `mocha test/*.ts --require ts-node/register` | 
| [Soluto/graphql-to-mongodb](https://github.com/Soluto/graphql-to-mongodb) | 106 | `ts-mocha tests/**/*.spec.ts` | 
| [moodysalem/react-tournament-bracket](https://github.com/moodysalem/react-tournament-bracket) | 106 | `mocha --require ts-node/register src/**/*.test.tsx` | 
| [materiahq/materia-server](https://github.com/materiahq/materia-server) | 106 | `mocha -R spec dist/test/**/*.js` | 
| [Enterprise-JS/vscode-ts-node-debugging](https://github.com/Enterprise-JS/vscode-ts-node-debugging) | 105 | `npm run mocha --recursive ./src/**/__tests__/*` | 
| [Microsoft/TypeScript-TmLanguage](https://github.com/Microsoft/TypeScript-TmLanguage) | 103 | `mocha --full-trace tests/test.js` | 
| [nestjs/typeorm](https://github.com/nestjs/typeorm) | 102 | `tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [bradymholt/cRonstrue](https://github.com/bradymholt/cRonstrue) | 101 | `npx mocha --reporter spec --compilers ts:ts-node/register` | 
| [toolness/p5.js-widget](https://github.com/toolness/p5.js-widget) | 101 | `webpack && mocha-phantomjs test/index.html` | 
| [rjmacarthy/express-typescript-starter](https://github.com/rjmacarthy/express-typescript-starter) | 100 | `mocha -r ts-node/register -w ./spec/**/*.spec.ts` | 
| [thomasboyt/manygolf](https://github.com/thomasboyt/manygolf) | 98 | `webpack --config webpack/test.js && mocha --no-colors build/test/test.bundle.js` | 
| [geofirestore/geofirestore-js](https://github.com/geofirestore/geofirestore-js) | 98 | `nyc --reporter=html --reporter=text mocha` | 
| [palantir/typesettable](https://github.com/palantir/typesettable) | 97 | `npm-run-all build test:mocha test:coverage lint` | 
| [palantir/react-layered-chart](https://github.com/palantir/react-layered-chart) | 96 | `mocha 'test/**/*.ts' && tslint --project tsconfig.json` | 
| [IBM/Decentralized-Energy-Composer](https://github.com/IBM/Decentralized-Energy-Composer) | 95 | `mocha --recursive -t 4000` | 
| [jf3096/json-typescript-mapper](https://github.com/jf3096/json-typescript-mapper) | 95 | `mocha ./spec/*.js` | 
| [tunnelvisionlabs/antlr4ts](https://github.com/tunnelvisionlabs/antlr4ts) | 95 | `mocha` | 
| [JoshGlazebrook/socks](https://github.com/JoshGlazebrook/socks) | 95 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [tycho01/typical](https://github.com/tycho01/typical) | 95 | `tsc | tee tsc.log && mocha lib/**/*.test.js 2>&1 | sed 's/[0-9]\+)/×/g' | tee errors.log` | 
| [motorcyclejs/motorcyclejs](https://github.com/motorcyclejs/motorcyclejs) | 95 | `northbrook tslint && northbrook mocha && northbrook karma` | 
| [metaes/metaes](https://github.com/metaes/metaes) | 94 | `tsc; mocha --recursive test/suite/` | 
| [filestack/filestack-js](https://github.com/filestack/filestack-js) | 94 | `npm run build && concurrently -r --kill-others 'npm run prism:mock' 'npm run toxy' 'npm run lint && TEST_ENV=unit karma start && TEST_ENV=unit nyc mocha'` | 
| [redhat-developer/yaml-language-server](https://github.com/redhat-developer/yaml-language-server) | 94 | `mocha --require ts-node/register --ui tdd ./test/*.test.ts` | 
| [rohitpaulk/todoist-tribute](https://github.com/rohitpaulk/todoist-tribute) | 93 | `mocha --compilers ts:ts-node/register app/javascript/packs/tests/**/*.ts` | 
| [philcockfield/storybook-host](https://github.com/philcockfield/storybook-host) | 93 | `./node_modules/mocha/bin/mocha --require ts-node/register --watch-extensions ts,tsx 'src/**/*.test.ts{,x}'` | 
| [InCar/ali-mns](https://github.com/InCar/ali-mns) | 93 | `node node_modules/mocha/bin/mocha` | 
| [functionalone/serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) | 92 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [matthew-matvei/freeman](https://github.com/matthew-matvei/freeman) | 91 | `xvfb-maybe electron-mocha --renderer __tests__` | 
| [any-json/any-json](https://github.com/any-json/any-json) | 91 | `npm run build && cp -Rf test/fixtures out/test/ && mocha --ui tdd out/test/` | 
| [Kode/KodeStudio](https://github.com/Kode/KodeStudio) | 91 | `mocha` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 90 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [horiuchi/dtsgenerator](https://github.com/horiuchi/dtsgenerator) | 90 | `istanbul cover _mocha test/*.js test/**/*.js` | 
| [AkashaProject/ipfs-connector](https://github.com/AkashaProject/ipfs-connector) | 90 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests.js` | 
| [structured-log/structured-log](https://github.com/structured-log/structured-log) | 90 | `mocha --compilers ts:ts-node/register -r src/polyfills/objectAssign.js test/**/*.spec.ts` | 
| [sudheerj/generator-jhipster-primeng](https://github.com/sudheerj/generator-jhipster-primeng) | 90 | `mocha test/* --timeout 500000` | 
| [englercj/tsd-jsdoc](https://github.com/englercj/tsd-jsdoc) | 89 | `mocha --ui tdd -r ts-node/register test/specs/**.ts` | 
| [secret-tech/backend-ico-dashboard](https://github.com/secret-tech/backend-ico-dashboard) | 89 | `nyc mocha ./src/**/*.spec.ts --require test/prepare.ts` | 
| [inversify/inversify-express-example](https://github.com/inversify/inversify-express-example) | 89 | `nyc --clean --all --require ts-node/register --require reflect-metadata/Reflect --extension .ts -- mocha --exit --timeout 5000` | 
| [KarlPurk/redux-decorators](https://github.com/KarlPurk/redux-decorators) | 88 | `webpack --env=test > /dev/null && mocha dist/redux-decorators.spec.js` | 
| [nicksenger/react-arcgis](https://github.com/nicksenger/react-arcgis) | 87 | `nyc mocha` | 
| [jvilk/MakeTypes](https://github.com/jvilk/MakeTypes) | 86 | `npm-run-all --serial prepublish generate:test build:test mocha` | 
| [ynab/ynab-sdk-js](https://github.com/ynab/ynab-sdk-js) | 86 | `TS_NODE_PROJECT=./test/tsconfig.json npx mocha --reporter spec --require ts-node/register 'test/**/*.ts'` | 
| [ENikS/LINQ](https://github.com/ENikS/LINQ) | 86 | `mocha test/ --recursive` | 
| [aurelia/vscode-extension](https://github.com/aurelia/vscode-extension) | 85 | `mocha ./dist/test --recursive` | 
| [gcanti/prop-types-ts](https://github.com/gcanti/prop-types-ts) | 84 | `npm run lint && npm run prettier && npm run mocha` | 
| [cartant/ts-action](https://github.com/cartant/ts-action) | 84 | `yarn run lint && yarn run test:build && mocha ./build/**/*-spec.js` | 
| [atomist/sdm](https://github.com/atomist/sdm) | 84 | `nyc mocha --require espower-typescript/guess --require source-map-support/register "test/**/*.test.ts"` | 
| [shlomiassaf/ngc-webpack](https://github.com/shlomiassaf/ngc-webpack) | 83 | `npm run build-test && ./node_modules/.bin/mocha dist/test/*.spec.js --recursive` | 
| [dsherret/ts-nameof](https://github.com/dsherret/ts-nameof) | 83 | `npm run --silent copy-test-files && nyc --reporter=lcov mocha --opts mocha.opts` | 
| [vladotesanovic/typescript-mongoose-express](https://github.com/vladotesanovic/typescript-mongoose-express) | 83 | `mocha` | 
| [carlansley/swagger2-koa](https://github.com/carlansley/swagger2-koa) | 83 | `npm run build && _mocha $(find build -name '*.spec.js') && npm run lint` | 
| [mysticatea/vue-eslint-parser](https://github.com/mysticatea/vue-eslint-parser) | 81 | `nyc npm run _mocha` | 
| [neon-bindings/neon-cli](https://github.com/neon-bindings/neon-cli) | 81 | `npm run transpile && mocha dist/neon-cli-test/acceptance` | 
| [flagello/Essence](https://github.com/flagello/Essence) | 78 | `mocha` | 
| [atlassian/nucleus](https://github.com/atlassian/nucleus) | 77 | `mocha --compilers ts:ts-node/register src/__spec__/rest.ts src/**/__spec__/*_spec.ts src/**/**/__spec__/*_spec.ts` | 
| [koltyakov/sp-rest-proxy](https://github.com/koltyakov/sp-rest-proxy) | 77 | `ts-node ./test/init && mocha --opts test/mocha.opts || ECHO.` | 
| [ajafff/tsutils](https://github.com/ajafff/tsutils) | 76 | `mocha test/*Tests.js && tslint --test 'test/rules/**/tslint.json'` | 
| [AlexGalays/spacelift](https://github.com/AlexGalays/spacelift) | 75 | `mocha test/test.js && mocha --ui tdd test/option.js && mocha --ui tdd test/result.js` | 
| [teambition/ReactiveDB](https://github.com/teambition/ReactiveDB) | 74 | `npm run lint && NODE_ENV=test tman --mocha spec-js/test/run.js` | 
| [wavesplatform/waves-api](https://github.com/wavesplatform/waves-api) | 74 | `npm run build && ./node_modules/.bin/tsc -p ./test/tsconfig.json && ./node_modules/.bin/mocha $(find ./tmp-node/test -name '*.spec.js')` | 
| [yakovlevga/brickyeditor](https://github.com/yakovlevga/brickyeditor) | 74 | `mocha --compilers js:babel-core/register --recursive` | 
| [rh389/dynamodb-geo.js](https://github.com/rh389/dynamodb-geo.js) | 74 | `mocha --require ts-node/register test/**/*.ts` | 
| [funkia/jabz](https://github.com/funkia/jabz) | 73 | `nyc mocha --recursive test/**/*.ts` | 
| [codius/codiusd](https://github.com/codius/codiusd) | 73 | `npm run lint && nyc mocha` | 
| [kimamula/ts-transformer-keys](https://github.com/kimamula/ts-transformer-keys) | 72 | `tsc && node ./test/compileMain.js && mocha ./test/main.js` | 
| [redhat-developer/vscode-yaml](https://github.com/redhat-developer/vscode-yaml) | 72 | `mocha --ui tdd out/test/extension.test.js` | 
| [suksant/sequelize-typescript-examples](https://github.com/suksant/sequelize-typescript-examples) | 71 | `gulp compile && mocha 'build/*/test/**/*.js'` | 
| [felixfbecker/sequelize-decorators](https://github.com/felixfbecker/sequelize-decorators) | 71 | `mocha dist/test` | 
| [hawx1993/judge](https://github.com/hawx1993/judge) | 70 | `mocha --compilers ts:ts-node/register test/test.ts` | 
| [gcanti/elm-ts](https://github.com/gcanti/elm-ts) | 70 | `npm run lint && npm run mocha` | 
| [httptoolkit/mockttp](https://github.com/httptoolkit/mockttp) | 70 | `npm run build && npm run test:mocha && npm run test:browser` | 
| [wbhob/nest-middlewares](https://github.com/wbhob/nest-middlewares) | 69 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [Microsoft/NoSQLProvider](https://github.com/Microsoft/NoSQLProvider) | 69 | `mocha dist/tests/NoSqlProviderTests.js --timeout 5000` | 
| [olosegres/jsona](https://github.com/olosegres/jsona) | 68 | `npm run test-compile && env NODE_ENV=test ts-mocha ./**/*.test.ts` | 
| [Team-CHAD/DevDecks](https://github.com/Team-CHAD/DevDecks) | 68 | `cross-env NODE_ENV=test NODE_PATH=./app BABEL_DISABLE_CACHE=1 mocha --retries 2 --compilers ts:ts-node/register --recursive --require ignore-styles ./test/setup.ts test/**/*.spec.ts test/**/*.spec.tsx` | 
| [indiejames/vscode-clojure-debug](https://github.com/indiejames/vscode-clojure-debug) | 68 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [Microsoft/vscode-chrome-debug-core](https://github.com/Microsoft/vscode-chrome-debug-core) | 68 | `mocha --exit --recursive -u tdd ./out/test/` | 
| [troch/path-parser](https://github.com/troch/path-parser) | 67 | `mocha -r ts-node/register 'test/main.js'` | 
| [Polymer/polymer-editor-service](https://github.com/Polymer/polymer-editor-service) | 67 | `npm run clean && npm run build && mocha && npm run lint` | 
| [mattlewis92/generator-angular-library](https://github.com/mattlewis92/generator-angular-library) | 66 | `NODE_ENV=test mocha --timeout 300000` | 
| [googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery) | 65 | `mocha build/test` | 
| [AugurProject/augur-node](https://github.com/AugurProject/augur-node) | 65 | `mocha test/unit` | 
| [jinhduong/linq-fns](https://github.com/jinhduong/linq-fns) | 65 | `mocha -r ts-node/register test/*.ts` | 
| [AlexGalays/immupdate](https://github.com/AlexGalays/immupdate) | 65 | `mocha test/test.js && node test/testCompilationErrors.js` | 
| [Microsoft/vscode-mock-debug](https://github.com/Microsoft/vscode-mock-debug) | 64 | `mocha -u tdd ./out/tests/` | 
| [ui-jar/ui-jar](https://github.com/ui-jar/ui-jar) | 64 | `tsc && mocha "dist/test/**/*.js" ` | 
| [wikiwi/reassemble](https://github.com/wikiwi/reassemble) | 64 | `cross-env TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --opts mocha.opts` | 
| [tinganho/node-accept-language](https://github.com/tinganho/node-accept-language) | 64 | `node node_modules/mocha/bin/mocha Build/Tests/Test.js` | 
| [Azure/azure-cosmos-js](https://github.com/Azure/azure-cosmos-js) | 63 | `mocha -r ./src/test/common/setup.ts ./lib/test/ --recursive --timeout 100000 -i -g .*ignore.js` | 
| [Microsoft/vscode-css-languageservice](https://github.com/Microsoft/vscode-css-languageservice) | 63 | `npm run compile && mocha && npm run lint` | 
| [mrmlnc/vscode-scss](https://github.com/mrmlnc/vscode-scss) | 63 | `mocha out/**/*.spec.js` | 
| [theGlenn/apollo-prophecy](https://github.com/theGlenn/apollo-prophecy) | 62 | `rm -rf coverage && nyc mocha --opts mocha.opts` | 
| [balassy/aws-lambda-typescript](https://github.com/balassy/aws-lambda-typescript) | 61 | `nyc mocha` | 
| [zenclabs/codetree](https://github.com/zenclabs/codetree) | 61 | `mocha -r ts-node/register src/**/*.spec.ts` | 
| [bespoken/virtual-alexa](https://github.com/bespoken/virtual-alexa) | 61 | `nyc mocha lib/**/*Test.js` | 
| [apollographql/graphql-document-collector](https://github.com/apollographql/graphql-document-collector) | 61 | `mocha 'lib/**/__tests__/*.js'` | 
| [HerringtonDarkholme/kilimanjaro](https://github.com/HerringtonDarkholme/kilimanjaro) | 61 | `mocha dist/test/*.js` | 
| [AndrewPoyntz/time-ago-pipe](https://github.com/AndrewPoyntz/time-ago-pipe) | 61 | `mocha --reporter spec --require ts-node/register test/**/*.spec.ts` | 
| [MariusAlch/json-to-ts](https://github.com/MariusAlch/json-to-ts) | 60 | `npm run build && mocha ./test/js-integration/index.js && mocha ./build/test` | 
| [wix/rawss](https://github.com/wix/rawss) | 60 | `mocha` | 
| [hbenl/vscode-firefox-debug](https://github.com/hbenl/vscode-firefox-debug) | 60 | `TS_NODE_FILES=true mocha --opts src/test/mocha.opts "src/test/test*.ts"` | 
| [metadevpro/openapi3-ts](https://github.com/metadevpro/openapi3-ts) | 60 | `mocha --recursive --compilers ts:ts-node/register --require source-map-support/register "src/**/*.spec.ts"` | 
| [Cody2333/koa-swagger-decorator](https://github.com/Cody2333/koa-swagger-decorator) | 59 | `./node_modules/mocha/bin/mocha -r babel-core/register test/**/*.js --bail -t 2000000` | 
| [NativeScript/nativescript-vscode-extension](https://github.com/NativeScript/nativescript-vscode-extension) | 59 | `mocha --opts ./src/tests/config/mocha.opts` | 
| [KoteiIto/node-athena](https://github.com/KoteiIto/node-athena) | 58 | `rm -rf coverage && istanbul cover _mocha -- -R spec build/test/*.js` | 
| [interledgerjs/ilp-connector](https://github.com/interledgerjs/ilp-connector) | 58 | `nyc mocha` | 
| [adrien2p/nestjs-graphql](https://github.com/adrien2p/nestjs-graphql) | 57 | `mocha -r ts-node/register src/**/tests/*.ts` | 
| [isc30/linq-collections](https://github.com/isc30/linq-collections) | 57 | `nyc mocha ./build/test/TestSuite.js --slow 0` | 
| [matthiasferch/tsm](https://github.com/matthiasferch/tsm) | 56 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [cartant/rxjs-etc](https://github.com/cartant/rxjs-etc) | 56 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [pact-foundation/pact-node](https://github.com/pact-foundation/pact-node) | 56 | `cross-env LOGLEVEL=debug PACT_DO_NOT_TRACK=true mocha -r ts-node/register -R mocha-unfunk-reporter -t 15000 -s 5000 -b --check-leaks --exit "{src,test,bin,standalone}/**/*.spec.ts"` | 
| [puzzle-js/PuzzleJs](https://github.com/puzzle-js/PuzzleJs) | 55 | `nyc --check-coverage --lines=85 cross-env NODE_ENV=production mocha -r ts-node/register  --recursive 'test/**/*.spec.ts'` | 
| [jeswin/basho](https://github.com/jeswin/basho) | 55 | `./build.sh && mocha dist/test/test.js` | 
| [19majkel94/class-transformer-validator](https://github.com/19majkel94/class-transformer-validator) | 55 | `mocha build/tests/index.js` | 
| [jupyter-attic/services](https://github.com/jupyter-attic/services) | 55 | `mocha --retries 3 test/build/**/*.spec.js --foo bar --terminalsAvailable True` | 
| [DavidDuwaer/Coloquent](https://github.com/DavidDuwaer/Coloquent) | 54 | `npm run build && mocha -r ts-node/register tests/**/*.test.ts` | 
| [akoenig/gulp-svg2png](https://github.com/akoenig/gulp-svg2png) | 54 | `npm run build && npm run mocha` | 
| [Microsoft/vscode-node-debug2](https://github.com/Microsoft/vscode-node-debug2) | 53 | `mocha --timeout 20000 -s 2000 -u tdd --colors --reporter node_modules/vscode-chrome-debug-core-testsupport/out/loggingReporter.js ./out/test/` | 
| [mrmlnc/emitty](https://github.com/mrmlnc/emitty) | 53 | `mocha out/test/{,**/}*.spec.js -s 0` | 
| [mceachen/exiftool-vendored.js](https://github.com/mceachen/exiftool-vendored.js) | 53 | `nyc mocha --opts .mocha.opts` | 
| [bougarfaoui/back](https://github.com/bougarfaoui/back) | 53 | `mocha` | 
| [googleapis/node-gtoken](https://github.com/googleapis/node-gtoken) | 53 | `nyc mocha build/test` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 52 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 52 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 52 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 52 | `mocha --timeout 30000 test/**/*.js` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 52 | `mocha --recursive` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 52 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 52 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 52 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [yagajs/leaflet-ng2](https://github.com/yagajs/leaflet-ng2) | 52 | `npm run lint && npm run transpile && istanbul cover _mocha -- -- test/*.js` | 
| [pdupavillon/express-recaptcha](https://github.com/pdupavillon/express-recaptcha) | 52 | `mocha --compilers ts:ts-node/register test/**/*.spec.ts` | 
| [AkashaProject/geth-connector](https://github.com/AkashaProject/geth-connector) | 52 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/.bin/_mocha  ./tests/index.js` | 
| [nicojs/node-install-local](https://github.com/nicojs/node-install-local) | 52 | `mocha --timeout 30000 test/**/*.js` | 
| [hazelcast/hazelcast-nodejs-client](https://github.com/hazelcast/hazelcast-nodejs-client) | 52 | `mocha --recursive` | 
| [argoproj/argo-ci](https://github.com/argoproj/argo-ci) | 52 | `TS_NODE_PROJECT=./src/tests/tsconfig.json mocha --require ts-node/register ./src/tests/**/*spec.ts` | 
| [ryanatkn/ear-sharpener](https://github.com/ryanatkn/ear-sharpener) | 52 | `NODE_ENV=test mocha --require ts-node/register --require ignore-styles --require src/test src/**/*/test.{ts,tsx}` | 
| [SqrTT/prophet](https://github.com/SqrTT/prophet) | 52 | `node ./node_modules/mocha/bin/mocha -u tdd ./out/tests/` | 
| [AmirTugi/tea-school](https://github.com/AmirTugi/tea-school) | 51 | `npx ts-mocha ./src/tests/**.ts` | 
| [vechain/thorify](https://github.com/vechain/thorify) | 51 | `NODE_ENV=test mocha --require ts-node/register --timeout 20000 --recursive  --exclude './test/browser/*.ts' './**/*.test.ts'` | 
| [WasabiFan/ev3dev-lang-js](https://github.com/WasabiFan/ev3dev-lang-js) | 51 | `grunt tsc && ./node_modules/mocha/bin/mocha` | 
| [JBlaak/Express-Torch](https://github.com/JBlaak/Express-Torch) | 51 | `yarn lint && yarn mocha` | 
| [sjohnsonaz/cascade](https://github.com/sjohnsonaz/cascade) | 50 | `tsc && node src/mocha/NodeRunner.js` | 
| [hcnode/koa-cola](https://github.com/hcnode/koa-cola) | 50 | `NODE_ENV=test nyc mocha` | 
| [tusharmath/rwc](https://github.com/tusharmath/rwc) | 50 | `tsc && mocha -r src/TestSetup.js` | 
| [soywiz/atpl.js](https://github.com/soywiz/atpl.js) | 50 | `tsc && ./node_modules/.bin/mocha --ui exports --globals name ` | 
| [evansolomon/nodejs-kinesis-client-library](https://github.com/evansolomon/nodejs-kinesis-client-library) | 49 | `npm run lint && mocha` | 
| [SomeKittens/gustav](https://github.com/SomeKittens/gustav) | 49 | `mocha dist/test` | 
| [indutny/llparse](https://github.com/indutny/llparse) | 49 | `npm run mocha && npm run lint` | 
| [ktsn/vuetype](https://github.com/ktsn/vuetype) | 49 | `rimraf test/fixtures/*.d.ts && mocha --require espower-typescript/guess test/specs/**/*.ts` | 
| [jsonapi-suite/jsorm](https://github.com/jsonapi-suite/jsorm) | 49 | `NODE_ENV=test mocha --opts test/mocha.opts` | 
| [deerawan/vscode-dash](https://github.com/deerawan/vscode-dash) | 49 | `./node_modules/istanbul/lib/cli.js cover ./node_modules/mocha/bin/_mocha -- -R spec --ui tdd ./out/test/extension.test.js` | 
| [DhyanaChina/todo-live](https://github.com/DhyanaChina/todo-live) | 49 | `mocha` | 
| [getsentry/sentry-electron](https://github.com/getsentry/sentry-electron) | 49 | `cross-env TS_NODE_PROJECT=tsconfig.json xvfb-maybe electron-mocha --require ts-node/register/transpile-only --timeout 3000 ./test/unit/**/*.ts` | 
| [infinum/mobx-jsonapi-store](https://github.com/infinum/mobx-jsonapi-store) | 48 | `NODE_ENV=test nyc mocha` | 
| [mike-lischke/antlr4-c3](https://github.com/mike-lischke/antlr4-c3) | 48 | `tsc --version && tsc && mocha out/test` | 
| [xmlking/koa-router-decorators](https://github.com/xmlking/koa-router-decorators) | 48 | `mocha .tmp/test/**/*.spec.js` | 
| [timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator) | 48 | `mocha --timeout 10000 --slow 2500 tests/all-test-cases.js` | 
| [Fundflow/apollo-redux-form](https://github.com/Fundflow/apollo-redux-form) | 47 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [tjson/tjson-js](https://github.com/tjson/tjson-js) | 47 | `mocha --compilers ts:ts-node/register --recursive` | 
| [grantila/fetch-h2](https://github.com/grantila/fetch-h2) | 47 | `node_modules/.bin/istanbul cover node_modules/.bin/_mocha -- --bail --check-leaks dist/test` | 
| [PeculiarVentures/xadesjs](https://github.com/PeculiarVentures/xadesjs) | 47 | `mocha` | 
| [rgraphql/soyuz](https://github.com/rgraphql/soyuz) | 47 | `npm run lint && npm run mocha` | 
| [stevenxie/express-starter](https://github.com/stevenxie/express-starter) | 47 | `NODE_ENV=test; npm run build; mocha -Sb --exit tests/*.test.js` | 
| [DhyanaChina/koa2-typescript-guide](https://github.com/DhyanaChina/koa2-typescript-guide) | 46 | `mocha` | 
| [sketchglass/respass](https://github.com/sketchglass/respass) | 46 | `NODE_ENV=test mocha lib/test` | 
| [thiagobustamante/typescript-rest-swagger](https://github.com/thiagobustamante/typescript-rest-swagger) | 45 | `cross-env NODE_ENV=test mocha` | 
| [shlomiassaf/ng-router-loader](https://github.com/shlomiassaf/ng-router-loader) | 45 | `npm run compile_integration && npm run build && ./node_modules/.bin/mocha dist/test spec --recursive` | 
| [longlho/ts-transform-css-modules](https://github.com/longlho/ts-transform-css-modules) | 45 | `rm -rf test/fixture/*.js && mocha --require ts-node/register --recursive  test/**/*.test.ts` | 
| [firebase/firebase-functions-test](https://github.com/firebase/firebase-functions-test) | 45 | `mocha .tmp/spec/index.spec.js` | 
| [SPGoding/spu](https://github.com/SPGoding/spu) | 45 | `mocha --require espower-typescript/guess "./src/tests/**/*.ts"` | 
| [rauschma/stringio](https://github.com/rauschma/stringio) | 44 | `mocha --ui qunit` | 
| [realm/realm-graphql](https://github.com/realm/realm-graphql) | 44 | `mocha --opts config/mocha.opts` | 
| [Anonyfox/vuex-store-module-example](https://github.com/Anonyfox/vuex-store-module-example) | 44 | `rm -rf dist && tsc -p . && npm run lint && mocha dist/test` | 
| [Microsoft/vscode-json-languageservice](https://github.com/Microsoft/vscode-json-languageservice) | 44 | `npm run compile && mocha && npm run lint` | 
| [rsamec/react-binding](https://github.com/rsamec/react-binding) | 44 | `mocha -R spec ./test` | 
| [duffman/tspath](https://github.com/duffman/tspath) | 44 | `mocha -r ts-node/register test/**.*/test.ts` | 
| [roginvs/space-rangers-quest](https://github.com/roginvs/space-rangers-quest) | 44 | `nyc --reporter=html --reporter=text mocha --bail built-node/test` | 
| [KennethanCeyer/formulize](https://github.com/KennethanCeyer/formulize) | 44 | `nyc mocha --opts test/mocha.opts` | 
| [HdrHistogram/HdrHistogramJS](https://github.com/HdrHistogram/HdrHistogramJS) | 43 | `mocha --opts mocha.opts --watch` | 
| [brunolm/ts-react-redux-startup](https://github.com/brunolm/ts-react-redux-startup) | 43 | `npm run lint && mocha dist/spec` | 
| [crescware/walts](https://github.com/crescware/walts) | 43 | `npm run build && mocha --require intelli-espower-loader --reporter dot ./test/test.js` | 
| [alex-okrushko/backoff-rxjs](https://github.com/alex-okrushko/backoff-rxjs) | 43 | `mocha --opts spec/mocha.opts spec/**/*-spec.ts` | 
| [mj1618/serverless-offline-sns](https://github.com/mj1618/serverless-offline-sns) | 43 | `nyc ts-mocha "test/**/*.ts" -p src/` | 
| [RobotlegsJS/RobotlegsJS](https://github.com/RobotlegsJS/RobotlegsJS) | 43 | `nyc mocha` | 
| [zswang/icity](https://github.com/zswang/icity) | 43 | `istanbul cover --hook-run-in-context node_modules/mocha/bin/_mocha -- -R spec` | 
| [fuse-box/angular2-example](https://github.com/fuse-box/angular2-example) | 43 | `cross-env TS_NODE_PROJECT=./src/tsconfig.mocha.json mocha --opts ./test/mocha.travis.opts` | 
| [balmbees/dynamo-typeorm](https://github.com/balmbees/dynamo-typeorm) | 43 | `AWS_REGION=us-east-1 AWS_ACCESS_KEY_ID=mock AWS_SECRET_ACCESS_KEY=mock DYNAMO_TYPES_ENDPOINT=http://127.0.0.1:8000 mocha -t 20000 dst/**/__test__/**/*.js` | 
| [w11k/ngx-componentdestroyed](https://github.com/w11k/ngx-componentdestroyed) | 42 | `mocha --opts spec/mocha.opts src/**/*test.ts` | 
| [TonyRobotics/RoboWare-Studio](https://github.com/TonyRobotics/RoboWare-Studio) | 42 | `mocha` | 
| [mrmlnc/vscode-csscomb](https://github.com/mrmlnc/vscode-csscomb) | 42 | `mocha out/{,**/}*.spec.js -s 0` | 
| [ikr/react-star-rating-input](https://github.com/ikr/react-star-rating-input) | 42 | `mocha -r ts-node/register -r tests/helpers/enzyme -b tests/*.spec.*` | 
| [rhysd/fixjson](https://github.com/rhysd/fixjson) | 42 | `mocha test` | 
| [Microsoft/node-jsonc-parser](https://github.com/Microsoft/node-jsonc-parser) | 41 | `npm run compile && mocha` | 
| [indutny/llhttp](https://github.com/indutny/llhttp) | 41 | `npm run mocha && npm run lint` | 
| [pubkey/solidity-cli](https://github.com/pubkey/solidity-cli) | 41 | `mocha --bail --exit ./dist/test/index.test.js  ./dist/test/integration.test.js` | 
| [bitjourney/ci-npm-update](https://github.com/bitjourney/ci-npm-update) | 41 | `TS_NODE_PROJECT=test/tsconfig.json mocha --opts test/support/default.opts test/**/*.test.ts` | 
| [ShyykoSerhiy/spotilocal](https://github.com/ShyykoSerhiy/spotilocal) | 41 | `./node_modules/typescript/bin/tsc && mocha "dist/test/**/*.js"` | 
| [darkoverlordofdata/entitas-ts](https://github.com/darkoverlordofdata/entitas-ts) | 41 | `NODE_ENV=test mocha --compilers coffee:coffee-script --require test/test_helper.js --recursive` | 
| [marcinnajder/powerseq](https://github.com/marcinnajder/powerseq) | 41 | `mocha ./dist/cjs_es6/test -R spec --recursive --timeout 30000` | 
| [ft-interactive/koa2-typescript-boilerplate](https://github.com/ft-interactive/koa2-typescript-boilerplate) | 41 | `tsc && mocha build/test` | 
| [ngParty/ts-helpers](https://github.com/ngParty/ts-helpers) | 41 | `mocha index.test.js` | 
| [mstssk/sw2dts](https://github.com/mstssk/sw2dts) | 40 | `mocha test/*.js` | 
| [JustinBeckwith/retry-axios](https://github.com/JustinBeckwith/retry-axios) | 40 | `nyc mocha build/test --timeout 5000 --require source-map-support/register` | 
| [dirk/hummingbird](https://github.com/dirk/hummingbird) | 40 | `node_modules/.bin/mocha` | 
| [sebawita/nativescript-angular-cli](https://github.com/sebawita/nativescript-angular-cli) | 40 | `istanbul cover node_modules/mocha/bin/_mocha -- --recursive --reporter spec-xunit-file --require test/test-bootstrap.js --timeout 1000 test/` | 
| [waitingsong/node-win32-api](https://github.com/waitingsong/node-win32-api) | 40 | `mocha --opts test/mocha.opts` | 
| [vilic/thenfail](https://github.com/vilic/thenfail) | 40 | `mocha && npm run aplus` | 
| [willryan/factory.ts](https://github.com/willryan/factory.ts) | 40 | `NODE_ENV=test mocha --require spec/setup.js --require ts-node/register` | 
| [AEB-labs/cruddl](https://github.com/AEB-labs/cruddl) | 40 | `tsc --noEmit --skipLibCheck && mocha --opts ./spec/mocha.opts` | 
| [Quramy/graphql-decorator](https://github.com/Quramy/graphql-decorator) | 40 | `npm run build && npm run lint && mocha lib/**/*.spec.js` | 
| [thundernet8/GithubProfile](https://github.com/thundernet8/GithubProfile) | 39 | `ts-mocha -p ./ test/**/*.spec.ts` | 
| [mshanemc/shane-sfdx-plugins](https://github.com/mshanemc/shane-sfdx-plugins) | 38 | `mocha --forbid-only "test/**/*.test.ts"` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 38 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 38 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 38 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 37 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 37 | `tsc && mocha dist/**/*.spec.js` | 
| [ngerakines/express-typescript-sequelize](https://github.com/ngerakines/express-typescript-sequelize) | 38 | `istanbul cover node_modules/mocha/bin/_mocha -x *.spec.js -- --reporter spec` | 
| [cartant/rxjs-observe](https://github.com/cartant/rxjs-observe) | 38 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [sourcegraph/sourcegraph-extension-api](https://github.com/sourcegraph/sourcegraph-extension-api) | 38 | `TS_NODE_COMPILER_OPTIONS='{"module":"commonjs"}' mocha --require ts-node/register --require source-map-support/register --opts mocha.opts` | 
| [AOEpeople/puppeteer-fetchbot](https://github.com/AOEpeople/puppeteer-fetchbot) | 37 | `npm run build && NODE_ENV=testing ./node_modules/.bin/mocha ./dist/lib/**/*.spec.js` | 
| [scopsy/node-typescript-starter](https://github.com/scopsy/node-typescript-starter) | 37 | `tsc && mocha dist/**/*.spec.js` | 
| [utopian-io/api.utopian.io](https://github.com/utopian-io/api.utopian.io) | 37 | `cross-env NODE_ENV=test npx mocha --ui bdd --reporter spec --colors --recursive -r ts-node/register tests/index.ts` | 
| [dalenguyen/firestore-backup-restore](https://github.com/dalenguyen/firestore-backup-restore) | 37 | `mocha --reporter spec` | 
| [sinnerschrader/aem-react-js](https://github.com/sinnerschrader/aem-react-js) | 37 | `npm run build && npm run lint &&  nyc mocha --compilers ts:espower-typescript/guess test/*.js ` | 
| [aiden/autobot](https://github.com/aiden/autobot) | 37 | `mocha --harmony --require source-map-support/register dist/test --recursive` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 36 | `tsc && npm run lint && mocha` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 36 | `npm run prettier && npm run lint && npm run mocha` | 
| [Polymer/polymer-linter](https://github.com/Polymer/polymer-linter) | 36 | `npm run build && mocha && npm run lint` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 36 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 36 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 36 | `mocha` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 36 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 36 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 36 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [OmniSharp/omnisharp-node-client](https://github.com/OmniSharp/omnisharp-node-client) | 36 | `tsc && npm run lint && mocha` | 
| [gcanti/io-ts-codegen](https://github.com/gcanti/io-ts-codegen) | 36 | `npm run prettier && npm run lint && npm run mocha` | 
| [Polymer/polymer-linter](https://github.com/Polymer/polymer-linter) | 36 | `npm run build && mocha && npm run lint` | 
| [zalando-incubator/authmosphere](https://github.com/zalando-incubator/authmosphere) | 36 | `npm run build && mocha lib/test lib/integration-test --recursive` | 
| [dupski/json-to-graphql-query](https://github.com/dupski/json-to-graphql-query) | 36 | `mocha -r ts-node/register --recursive "./src/**/__tests__/*"` | 
| [RobinBuschmann/react.di](https://github.com/RobinBuschmann/react.di) | 36 | `mocha` | 
| [chanlito/simple-todos](https://github.com/chanlito/simple-todos) | 36 | `cross-env NODE_ENV=test nyc mocha --require test/index.ts --opts test/mocha.opts` | 
| [zaaack/inker](https://github.com/zaaack/inker) | 36 | `electron-mocha --renderer -r ./tools/register "src/test/**.test.ts"` | 
| [usm4n/cycle-hn](https://github.com/usm4n/cycle-hn) | 36 | `cross-env NODE_ENV=test nyc mocha-webpack --timeout=100000 --colors --webpack-config configs/webpack.config.test.js test/**/*.test.*` | 
| [snaptopixel/vuex-ts-decorators](https://github.com/snaptopixel/vuex-ts-decorators) | 35 | `mocha -r source-map-support/register -r ts-node/register -r es6-promise/auto test/**/*.ts` | 
| [fyndme/messenger-bot-tester](https://github.com/fyndme/messenger-bot-tester) | 35 | `mocha ./test-build` | 
| [nickpisacane/mips](https://github.com/nickpisacane/mips) | 35 | `__TS_PROJECT_PATH__=./test ts-mocha test/**/*.test.ts` | 
| [tgreyuk/typedoc-plugin-markdown](https://github.com/tgreyuk/typedoc-plugin-markdown) | 35 | `mocha test/test.js` | 
| [ivarvh/movielistr-backend-ts-ioc](https://github.com/ivarvh/movielistr-backend-ts-ioc) | 34 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [JoshGlazebrook/smart-buffer](https://github.com/JoshGlazebrook/smart-buffer) | 34 | `NODE_ENV=test mocha --recursive --compilers ts:ts-node/register test/**/*.ts` | 
| [Draccoz/twc](https://github.com/Draccoz/twc) | 34 | `npm run lint && mocha --require ts-node/register --ui bdd tests/tests.spec.ts` | 
| [camesine/Typescript-restful-starter](https://github.com/camesine/Typescript-restful-starter) | 34 | `cross-env NODE_ENV=test nyc mocha test/**/*.ts` | 
| [davetemplin/web-request](https://github.com/davetemplin/web-request) | 34 | `mocha` | 
| [forthright/vile](https://github.com/forthright/vile) | 34 | `globstar -- _mocha "test/spec/**/*.coffee"` | 
| [paralin/grpc-bus](https://github.com/paralin/grpc-bus) | 34 | `npm run lint && npm run mocha` | 
| [qtumproject/qtumjs](https://github.com/qtumproject/qtumjs) | 34 | `mocha  lib/*_test.js` | 
| [jaystack/odata-v4-server](https://github.com/jaystack/odata-v4-server) | 34 | `nyc mocha --reporter mochawesome --reporter-options reportDir=report,reportName=odata-v4-server,reportTitle="OData V4 Server" src/test/**/*.spec.ts` | 
| [infinum/mobx-collection-store](https://github.com/infinum/mobx-collection-store) | 34 | `NODE_ENV=test nyc mocha` | 
| [realm/realm-graphql-service](https://github.com/realm/realm-graphql-service) | 33 | `mocha --opts ./mocha.opts` | 
| [aleris/zxing-typescript](https://github.com/aleris/zxing-typescript) | 33 | `mocha --compilers js:babel-core/register "build-node/test/core/**/*.js" --timeout 30000 --colors` | 
| [prismicio/prismic-javascript](https://github.com/prismicio/prismic-javascript) | 33 | `mocha` | 
| [evebook/api](https://github.com/evebook/api) | 33 | `nyc --require ts-node/register mocha src/**/*.spec.ts --reporter spec` | 
| [agea/CmisJS](https://github.com/agea/CmisJS) | 33 | `tsc && mocha dist/**/*.spec.js` | 
| [soraping/koa-ts](https://github.com/soraping/koa-ts) | 33 | `mocha --recursive` | 
| [szdc/tiktok-api](https://github.com/szdc/tiktok-api) | 33 | `mocha` | 
| [userpixel/typescript](https://github.com/userpixel/typescript) | 33 | `mocha test` | 
| [unbounce/iidy](https://github.com/unbounce/iidy) | 33 | `mocha lib/tests/_init.js lib/tests/**/*js` | 
| [indutny/bitcode](https://github.com/indutny/bitcode) | 33 | `npm run mocha && npm run lint` | 
| [microsoftgraph/msgraph-typescript-typings](https://github.com/microsoftgraph/msgraph-typescript-typings) | 33 | `tsc && mocha spec/` | 
| [supergraphql/supergraph](https://github.com/supergraphql/supergraph) | 33 | `nyc mocha ./dist/**/*.spec.js` | 
| [mixi-inc/css-semdiff](https://github.com/mixi-inc/css-semdiff) | 32 | `mocha --opts mocha.opts './dist/**/*.test.js'` | 
| [Jiasm/typescript-example](https://github.com/Jiasm/typescript-example) | 32 | `mocha -r ts-node/register test/**/*.spec.ts` | 
| [igorzg/typeix](https://github.com/igorzg/typeix) | 32 | `npm run compile && mocha build/tests/ --debug --full-trace` | 
| [breakstring/xunfeisdk](https://github.com/breakstring/xunfeisdk) | 32 | `tsc && mocha -R nyan -t 15000 -r ts-node/register "./test/**/*.ts"` | 
| [GoodgameStudios/RobotlegsJS](https://github.com/GoodgameStudios/RobotlegsJS) | 32 | `nyc mocha` | 
| [danrevah/typeserializer](https://github.com/danrevah/typeserializer) | 32 | `NODE_ENV=test mocha -r ts-node/register src/*.spec.ts src/**/*.spec.ts` | 
| [argoproj/argo-ui](https://github.com/argoproj/argo-ui) | 31 | `mocha --require ts-node/register ./src/app/**/*.spec.ts` | 
| [NikitchenkoSergey/scheme-designer](https://github.com/NikitchenkoSergey/scheme-designer) | 31 | `mocha` | 
| [tsframework/ts-framework](https://github.com/tsframework/ts-framework) | 31 | `mocha build-test --recursive` | 
| [ForbesLindesay/barrage](https://github.com/ForbesLindesay/barrage) | 31 | `mocha -R spec lib/test.js` | 
| [davetemplin/async-parallel](https://github.com/davetemplin/async-parallel) | 31 | `mocha` | 
| [home-assistant/home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | 31 | `mocha` | 
| [mulesoft-labs/yaml-ast-parser](https://github.com/mulesoft-labs/yaml-ast-parser) | 31 | `npm run build && mocha --ui tdd dist/test` | 
| [bpowers/sd.js](https://github.com/bpowers/sd.js) | 31 | `tsc -p .tsconfig.test.json && mocha` | 
| [Jason3S/rx-stream](https://github.com/Jason3S/rx-stream) | 31 | `mocha --recursive "dist/**/*.test.js"` | 
| [Rich-Harris/port-authority](https://github.com/Rich-Harris/port-authority) | 31 | `mocha --opts mocha.opts` | 
| [realm/realm-studio](https://github.com/realm/realm-studio) | 31 | `mocha-webpack --opts=configs/mocha-webpack.opts` | 
| [KennethanCeyer/browser-detect](https://github.com/KennethanCeyer/browser-detect) | 31 | `nyc mocha` | 
| [mrmlnc/vscode-stylefmt](https://github.com/mrmlnc/vscode-stylefmt) | 30 | `mocha out/**/*.spec.js -s 0` | 
| [leizongmin/leizm-web](https://github.com/leizongmin/leizm-web) | 30 | `npm run format && mocha --require ts-node/register --exit "src/test/**/*.ts"` | 
| [rhysd/electron-in-page-search](https://github.com/rhysd/electron-in-page-search) | 30 | `electron-mocha --timeout 10000 --renderer test/*.js` | 
| [haoliangyu/boundary.now](https://github.com/haoliangyu/boundary.now) | 30 | `mocha test/**/*.test.ts --require ts-node/register --require reflect-metadata` | 
| [siegebell/vsc-prettify-symbols-mode](https://github.com/siegebell/vsc-prettify-symbols-mode) | 30 | `tsc -p ./ && mocha -u tdd ./out/test` | 
| [secret-tech/backend-token-wallets](https://github.com/secret-tech/backend-token-wallets) | 30 | `mocha -r ts-node/register -r test/prepare.ts src/**/*.spec.ts` | 
| [Azure/oav](https://github.com/Azure/oav) | 29 | `npm run tsc && npm run tslint && nyc mocha ./test/**/*.ts -r ts-node/register -t 10000` | 
| [gwuhaolin/spring-data-rest-js](https://github.com/gwuhaolin/spring-data-rest-js) | 29 | `tsc & mocha` | 
| [Unibeautify/vscode](https://github.com/Unibeautify/vscode) | 29 | `mocha` | 
| [creeperyang/id3-parser](https://github.com/creeperyang/id3-parser) | 29 | `TS_NODE_PROJECT='test/tsconfig.json' mocha --require ts-node/register 'test/*.spec.ts' --reporter dot` | 
| [codefoster/waterrower](https://github.com/codefoster/waterrower) | 29 | `mocha test` | 
| [nicolastakashi/linq-to-type](https://github.com/nicolastakashi/linq-to-type) | 29 | `nyc mocha` | 
| [nilobarp/text2json](https://github.com/nilobarp/text2json) | 29 | `DEBUG=TP* mocha dist/test/spectrum-tests.js` | 
| [googleapis/google-cloud-kvstore](https://github.com/googleapis/google-cloud-kvstore) | 29 | `nyc mocha build/test` | 
| [ShieldBattery/node-interval-tree](https://github.com/ShieldBattery/node-interval-tree) | 29 | `mocha -R spec --compilers ts:ts-node/register test/*.ts` | 
| [palmerabollo/bingspeech-api-client](https://github.com/palmerabollo/bingspeech-api-client) | 29 | `npm run build && mocha -R spec 'lib/**/*.spec.js'` | 
| [3VLINC/graphql-to-typescript](https://github.com/3VLINC/graphql-to-typescript) | 29 | `mocha "dist/**/*.test.js"` | 
| [huang6349/ts-dva](https://github.com/huang6349/ts-dva) | 29 | `atool-test-mocha ./src/**/*-test.js` | 
| [alitaheri/jss-rtl](https://github.com/alitaheri/jss-rtl) | 29 | `mocha --require ts-node/register "src/**/*.spec.ts"` | 
| [coderfox/clover](https://github.com/coderfox/clover) | 29 | `nyc mocha` | 
| [dhruvrajvanshi/ts-failable](https://github.com/dhruvrajvanshi/ts-failable) | 29 | `mocha --compilers ts:ts-node/register './test/**/*[tj]s'` | 
| [ninoseki/mitaka](https://github.com/ninoseki/mitaka) | 29 | `nyc mocha -r ts-node/register "src/**/*.spec.ts"` | 
| [patrimart/monadness-js](https://github.com/patrimart/monadness-js) | 29 | `./node_modules/.bin/istanbul cover ./node_modules/mocha/bin/_mocha --report lcovonly -- -R spec && cat ./coverage/lcov.info | ./node_modules/coveralls/bin/coveralls.js && rm -rf ./coverage` | 
| [mseemann/js-restful-express](https://github.com/mseemann/js-restful-express) | 28 | `istanbul cover node_modules/mocha/bin/_mocha --report lcov -x '*.spec.*'  -- -c --check-leaks --require ts-node/register --require core-js --recursive --reporter spec src/**/*.spec.ts` | 
| [bespoken/virtual-device-sdk](https://github.com/bespoken/virtual-device-sdk) | 28 | `nyc mocha lib/test/*Test.js` | 
| [veonim/veonim](https://github.com/veonim/veonim) | 28 | `mocha test/unit` | 
| [ERCdEX/automation-toolkit](https://github.com/ERCdEX/automation-toolkit) | 28 | `rm -rf ./test-data && NODE_ENV=test mocha -t 15000 -r ts-node/register src/**/*.spec.ts` | 
| [NE-LOAN-FED/NE-Component](https://github.com/NE-LOAN-FED/NE-Component) | 28 | `mocha --compilers js:babel-register --recursive` | 
| [georgehanson/Vue-Form-Components](https://github.com/georgehanson/Vue-Form-Components) | 28 | `mocha-webpack --webpack-config="webpack.test.config.js" --require="tests/setup.ts" tests/**/*.spec.ts` | 
| [tbluemel/rtf.js](https://github.com/tbluemel/rtf.js) | 28 | `mocha test/test.js` | 
| [VaclavObornik/di-ts](https://github.com/VaclavObornik/di-ts) | 28 | `node ./node_modules/mocha/bin/mocha ./spec/ --recursive --require reflect-metadata` | 
| [AsynkronIT/protoactor-js](https://github.com/AsynkronIT/protoactor-js) | 27 | `mocha --opts test/mocha.opts -w` | 
| [acrazing/mobx-sync](https://github.com/acrazing/mobx-sync) | 27 | `mocha --require ts-node/register --slow 1000 ./src/**/*.spec.ts` | 
| [cartant/firebase-nightlight](https://github.com/cartant/firebase-nightlight) | 27 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [fsahmad/typescript-uml](https://github.com/fsahmad/typescript-uml) | 27 | `npm run build && mocha --compilers ts:ts-node/register --recursive 'src/**/*-spec.ts'` | 
| [RxParse/Parse-SDK-ts](https://github.com/RxParse/Parse-SDK-ts) | 27 | `node .bin/test/utils/init.js && mocha --timeout 30000 $(find .bin/test -name '*.js')` | 
| [lazerwalker/storyboard](https://github.com/lazerwalker/storyboard) | 27 | `mocha-webpack tests` | 
| [exercism/typescript](https://github.com/exercism/typescript) | 27 | `mocha test` | 
| [functionalone/aws-least-privilege](https://github.com/functionalone/aws-least-privilege) | 27 | `nyc mocha --require ts-node/register --require source-map-support/register  ./src/test/**/*.test.ts` | 
| [masvis/angular4-hal](https://github.com/masvis/angular4-hal) | 27 | `mocha -r ts-node/register --config=test/test-config.json test/*.test.ts` | 
| [ClickerMonkey/vuex-router-actions](https://github.com/ClickerMonkey/vuex-router-actions) | 27 | `mocha -r ts-node/register tests/**/*.ts` | 
| [TomShacham/http4js](https://github.com/TomShacham/http4js) | 27 | `tsc; mocha --require ts-node/register 'src/{test,ssl}/**/*.ts'` | 
| [vrudikov/typescript-rest-boilerplate](https://github.com/vrudikov/typescript-rest-boilerplate) | 27 | `cross-env NODE_ENV=test mocha` | 
| [alexeagle/tsetse](https://github.com/alexeagle/tsetse) | 26 | `tsc && mocha built/test/*.js` | 