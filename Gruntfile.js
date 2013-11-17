module.exports = function(grunt) {

  grunt.initConfig({
    coffee: {
      app: {
        expand: true,
        cwd: 'src/js',
        src: ['**/*.coffee'],
        dest: '.tmp/js',
        ext: '.js'
      }
    },
    concat: {
      options: {
        separator: ';',
      },
      dist: {
        src: [
          'node_modules/Flat-UI/js/bootstrap-select.js',
          'node_modules/Flat-UI/js/bootstrap-switch.js',
          'node_modules/Flat-UI/js/flatui-radio.js',
          'node_modules/Flat-UI/js/jquery.tagsinput.js',
          'node_modules/Flat-UI/js/jquery.stacktable.js',
          '.tmp/js/**/*.js'
        ],
        dest: '.tmp/application.js',
      },
    },
    uglify: {
      options: {
        banner: '/*! Built with Grunt */',
        compress: false
      },
      app: {
        src: ['.tmp/application.js'],
        dest: 'app/static/js/application.js',
      }
    },
    copy: {
      pre: {
        expand: true,
        cwd: 'src/css/flat-ui-override',
        dest: 'node_modules/Flat-UI/less',
        src: ['*.*']
      },
      post: {
        expand: true,
        cwd: 'node_modules/Flat-UI/fonts',
        dest: 'app/static/fonts',
        src: ['*.*']
      },
    },
    less: {
      production: {
        options: {
          yuicompress: true
        },
        files: {
          "app/static/css/style.css": "src/css/style.less"
        }
      }
    },
    clean: ['.tmp']
  });

  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-concat');

  grunt.registerTask('default', ['clean', 'copy:pre', 'less', 'coffee', 'concat', 'uglify', 'copy:post']);

};