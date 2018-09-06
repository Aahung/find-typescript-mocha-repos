# Find Repos in TypeScript Tested using Mocha

The list was updated at 00:44:32 09/06/18 PDT

## Requirements

```sh
pip install requests
```

## Repo List

| Repo | Stars | Test Script |
| --- | --- | --- |
| [Microsoft/vscode](https://github.com/Microsoft/vscode) | 58620 | `mocha` | 
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 14632 | `cross-env TS_NODE_PROJECT=spec/tsconfig.json mocha --opts spec/support/default.opts "spec/**/*-spec.ts"` | 
| [nestjs/nest](https://github.com/nestjs/nest) | 8347 | `nyc --require ts-node/register mocha packages/**/*.spec.ts --reporter spec` | 
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 8010 | `tsc && mocha --file ./build/compiled/test/utils/test-setup.js --bail --recursive --timeout 30000  ./build/compiled/test` | 
| [google/google-api-nodejs-client](https://github.com/google/google-api-nodejs-client) | 6707 | `nyc mocha build/test` | 
| [nexe/nexe](https://github.com/nexe/nexe) | 5476 | `mocha` | 
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | 4654 | `npm-run-all mocha lint` | 
| [Microsoft/sqlopsstudio](https://github.com/Microsoft/sqlopsstudio) | 4275 | `mocha` | 
| [palantir/tslint](https://github.com/palantir/tslint) | 3891 | `npm-run-all test:pre -p test:mocha test:rules` | 
| [williamngan/pts](https://github.com/williamngan/pts) | 3154 | `mocha --opts mocha.opts` | 
| [michaelgrosner/tribeca](https://github.com/michaelgrosner/tribeca) | 2716 | `mocha` | 
| [davidkpiano/xstate](https://github.com/davidkpiano/xstate) | 2401 | `npm run build:cjs && mocha --require ts-node/register test/**.ts test/**/*.test.ts` | 
| [decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate) | 2392 | `mocha 'test/**/*.ts'` | 
| [vuejs/vue-class-component](https://github.com/vuejs/vue-class-component) | 2309 | `npm run build && webpack --config test/webpack.config.js && mocha test/test.build.js` | 
| [compodoc/compodoc](https://github.com/compodoc/compodoc) | 1942 | `./node_modules/.bin/mocha-parallel-tests test && node test/dist/cli/cli-revert-root-folder.js` | 
| [thx/rap2-delos](https://github.com/thx/rap2-delos) | 1924 | `cross-env NODE_ENV=development cross-env TEST_MODE=true nyc mocha --exit` | 
| [yortus/asyncawait](https://github.com/yortus/asyncawait) | 1785 | `mocha` | 
| [mgechev/codelyzer](https://github.com/mgechev/codelyzer) | 1761 | `rimraf dist && tsc && ncp test/fixtures dist/test/fixtures && mocha dist/test --recursive` | 
| [s-panferov/awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) | 1695 | `rimraf .test && mocha --trace-warnings --timeout 30000 --exit dist/__test__` | 
| [staltz/xstream](https://github.com/staltz/xstream) | 1640 | `npm run lint && npm run test-types && npm run mocha && npm run doctest` | 
| [Microsoft/vscode-chrome-debug](https://github.com/Microsoft/vscode-chrome-debug) | 1302 | `mocha --exit --timeout 20000 -s 2000 -u tdd --colors "./out/test/*.test.js"` | 
| [Polymer/polymer-bundler](https://github.com/Polymer/polymer-bundler) | 1234 | `tsc && tslint -c tslint.json src/*.ts src/**/*.ts && mocha` | 
| [vscode-icons/vscode-icons](https://github.com/vscode-icons/vscode-icons) | 1186 | `nyc -x '' mocha` | 
| [funkia/list](https://github.com/funkia/list) | 1171 | `nyc mocha --timeout 10000 --recursive test/*.ts` | 
| [gamestdio/colyseus](https://github.com/gamestdio/colyseus) | 1158 | `mocha --require ts-node/register test/**Test.ts --exit` | 
| [jakubroztocil/rrule](https://github.com/jakubroztocil/rrule) | 1110 | `TS_NODE_PROJECT=tsconfig.test.json mocha **/*.test.ts` | 
| [watson-developer-cloud/node-sdk](https://github.com/watson-developer-cloud/node-sdk) | 1104 | `nyc mocha test/unit/ test/integration/ && nyc report --reporter=html` | 
| [firebase/geofire-js](https://github.com/firebase/geofire-js) | 1070 | `nyc --reporter=html --reporter=text mocha` | 
| [sveltejs/sapper](https://github.com/sveltejs/sapper) | 1032 | `mocha --opts mocha.opts` | 
| [Keyang/node-csvtojson](https://github.com/Keyang/node-csvtojson) | 1027 | `rm -Rf .ts-node && TS_NODE_CACHE_DIRECTORY=.ts-node mocha -r ts-node/register src/**/*.test.ts ./test/*.ts -R spec` | 
| [extrabacon/python-shell](https://github.com/extrabacon/python-shell) | 973 | `tsc -p ./ && mocha -R spec` | 
| [itchio/itch](https://github.com/itchio/itch) | 904 | `cross-env TS_NODE_PROJECT=tsconfig.test.json mocha -r ts-node/register -r tsconfig-paths/register ./src/**/*.spec.ts` | 
| [WuTheFWasThat/vimflowy](https://github.com/WuTheFWasThat/vimflowy) | 896 | `mocha --opts test/mocha.opts` | 
| [strongloop/loopback-next](https://github.com/strongloop/loopback-next) | 793 | `node packages/build/bin/run-nyc npm run mocha --scripts-prepend-node-path` | 
| [mgechev/ngrev](https://github.com/mgechev/ngrev) | 759 | `electron-mocha app/specs.js.autogenerated --renderer --require source-map-support/register` | 
| [Microsoft/dts-gen](https://github.com/Microsoft/dts-gen) | 728 | `mocha bin/tests/test.js` | 
| [coinbase/gdax-tt](https://github.com/coinbase/gdax-tt) | 714 | `yarn run lint && yarn run test:mocha` | 
| [angular/dgeni](https://github.com/angular/dgeni) | 701 | `mocha --require ts-node/register -R spec src/**/*.spec.ts` | 
| [google/clasp](https://github.com/google/clasp) | 690 | `nyc --cache false mocha --timeout 100000 -- tests/*.js` | 
| [iotaledger/iota.js](https://github.com/iotaledger/iota.js) | 659 | `mocha` | 
| [laoqiren/mlhelper](https://github.com/laoqiren/mlhelper) | 641 | `mocha --recursive` | 
| [simonbengtsson/jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) | 633 | `mocha --compilers ts:ts-node/register test/*.js || true` | 
| [ClusterWS/ClusterWS](https://github.com/ClusterWS/ClusterWS) | 631 | `mocha -r ts-node/register ./tests/specs/*.spec.ts --exit` | 
| [rubyide/vscode-ruby](https://github.com/rubyide/vscode-ruby) | 615 | `node ./node_modules/mocha/bin/mocha --recursive ./out/*.test.js` | 
| [davidkpiano/flipping](https://github.com/davidkpiano/flipping) | 605 | `NODE_ENV=test && mocha -r ts-node/register test/**.test.ts` | 
| [jaysoo/todomvc-redux-react-typescript](https://github.com/jaysoo/todomvc-redux-react-typescript) | 592 | `tsc && mocha --require test-setup --recursive ./dist/**/__spec__/**/*-spec.js` | 
| [alexjlockwood/avocado](https://github.com/alexjlockwood/avocado) | 590 | `./node_modules/.bin/mocha --require ts-node/register ./test/**/*.spec.ts` | 
| [hacksparrow/node-easyimage](https://github.com/hacksparrow/node-easyimage) | 585 | `npm run lint && npm run mocha` | 
| [mrmlnc/fast-glob](https://github.com/mrmlnc/fast-glob) | 563 | `mocha "out/**/*.spec.js" -s 0` | 
| [emilioastarita/lyricfier](https://github.com/emilioastarita/lyricfier) | 530 | `mocha` | 
| [SierraSoftworks/Iridium](https://github.com/SierraSoftworks/Iridium) | 526 | `mocha --opts test/mocha.opts dist/test` | 
| [rill-js/rill](https://github.com/rill-js/rill) | 522 | `nyc --extension=.ts --include=src/**/*.ts --reporter=lcov --reporter=text-summary npm run mocha` | 
| [opentracing/opentracing-javascript](https://github.com/opentracing/opentracing-javascript) | 516 | `mocha lib/test/unittest.js --check-leaks --color` | 
| [RxJS-CN/RxJS-Docs-CN](https://github.com/RxJS-CN/RxJS-Docs-CN) | 507 | `npm-run-all clean_spec build_spec test_mocha clean_spec` | 
| [data-forge/data-forge-ts](https://github.com/data-forge/data-forge-ts) | 471 | `nyc mocha --opts ./src/test/mocha.opts` | 
| [andrerpena/react-mde](https://github.com/andrerpena/react-mde) | 468 | `mocha --timeout 15000 -r ts-node/register ./test/*Spec.ts` | 
| [43081j/rar.js](https://github.com/43081j/rar.js) | 458 | `npm run build && mocha` | 
| [incrediblesound/story-graph](https://github.com/incrediblesound/story-graph) | 441 | `_mocha --` | 
| [electron/electron-rebuild](https://github.com/electron/electron-rebuild) | 430 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [YousefED/typescript-json-schema](https://github.com/YousefED/typescript-json-schema) | 423 | `npm run build && mocha -t 5000 --require source-map-support/register test` | 
| [szwacz/fs-jetpack](https://github.com/szwacz/fs-jetpack) | 417 | `mocha -r ts-node/register "spec/**/*.spec.ts"` | 
| [steelsojka/lodash-decorators](https://github.com/steelsojka/lodash-decorators) | 411 | `mocha --opts mocha.opts` | 
| [firebase/firebase-functions](https://github.com/firebase/firebase-functions) | 402 | `npm run mocha` | 
| [vvakame/typescript-formatter](https://github.com/vvakame/typescript-formatter) | 389 | `npm run build && mocha --reporter spec --timeout 20000 --require intelli-espower-loader` | 
| [Microsoft/vscode-pull-request-github](https://github.com/Microsoft/vscode-pull-request-github) | 387 | `tsc -p ./ && node ./node_modules/mocha/bin/_mocha --timeout 1000 --colors ./out/test/**/*.js` | 
| [Asana/typed-react](https://github.com/Asana/typed-react) | 384 | `istanbul cover _mocha -- --reporter ${MOCHA_REPORTER-nyan} --slow 10 --ui tdd --recursive build/**/*_test.js` | 
| [surf-build/surf](https://github.com/surf-build/surf) | 384 | `mocha --compilers ts:ts-node/register ./test/*.ts` | 
| [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js) | 377 | `nyc --check-coverage --reporter=html --reporter=text-summary mocha` | 
| [lukeautry/tsoa](https://github.com/lukeautry/tsoa) | 374 | `cross-env NODE_ENV=test mocha **/*.spec.ts --compilers ts:ts-node/register` | 
| [Romakita/ts-express-decorators](https://github.com/Romakita/ts-express-decorators) | 371 | `npm run clean && npm run tsc && npm run tslint && cross-env NODE_ENV=test nyc --reporter=html --reporter=text _mocha --recursive` | 
| [sourcegraph/javascript-typescript-langserver](https://github.com/sourcegraph/javascript-typescript-langserver) | 369 | `mocha --require source-map-support/register --timeout 7000 --slow 2000 lib/test/**/*.js` | 
| [felixfbecker/vscode-php-debug](https://github.com/felixfbecker/vscode-php-debug) | 367 | `mocha out/test --timeout 20000 --slow 1000 --retries 4` | 
| [jacobbogers/libRmath.js](https://github.com/jacobbogers/libRmath.js) | 359 | `cross-env-shell NODE_ENV=test TS_NODE_DISABLE_WARNINGS=true nyc mocha` | 
| [itsFrank/vue-typescript](https://github.com/itsFrank/vue-typescript) | 357 | `mocha` | 
| [Rich-Harris/devalue](https://github.com/Rich-Harris/devalue) | 350 | `mocha --opts mocha.opts` | 
| [ngParty/ng-metadata](https://github.com/ngParty/ng-metadata) | 345 | `mocha ./test/index.ts --require ts-node/register --colors --watch-extensions ts` | 
| [line/line-bot-sdk-nodejs](https://github.com/line/line-bot-sdk-nodejs) | 345 | `API_BASE_URL=http://localhost:1234/ TEST_PORT=1234 TS_NODE_CACHE=0 nyc mocha` | 
| [dsherret/ts-simple-ast](https://github.com/dsherret/ts-simple-ast) | 340 | `cross-env TS_NODE_COMPILER="ttypescript" mocha --opts mocha.opts` | 
| [Polymer/prpl-server](https://github.com/Polymer/prpl-server) | 332 | `npm run build && mocha` | 
| [championswimmer/vuex-persist](https://github.com/championswimmer/vuex-persist) | 323 | `node_modules/.bin/_mocha --require ts-node/register test/**/*.ts` | 
| [arangodb/arangojs](https://github.com/arangodb/arangojs) | 315 | `mocha --growl --reporter spec --require source-map-support/register --timeout 10000 lib/async/test` | 
| [apollographql/persistgraphql](https://github.com/apollographql/persistgraphql) | 311 | `mocha --reporter spec --full-trace lib/test/tests.js` | 
| [FinNLP/en-inflectors](https://github.com/FinNLP/en-inflectors) | 288 | `mocha` | 
| [cartant/rxjs-spy](https://github.com/cartant/rxjs-spy) | 281 | `yarn run lint && yarn run test:build && yarn run test:karma && yarn run test:mocha` | 
| [alexcambose/motus](https://github.com/alexcambose/motus) | 276 | `cross-env mocha -r ts-node/register 'test/**/*.spec.ts'` | 
| [biesbjerg/ngx-translate-extract](https://github.com/biesbjerg/ngx-translate-extract) | 274 | `mocha -r ts-node/register tests/**/*.spec.ts` | 
| [Microsoft/node-pty](https://github.com/Microsoft/node-pty) | 272 | `cross-env NODE_ENV=test mocha -R spec --exit lib/*.test.js` | 